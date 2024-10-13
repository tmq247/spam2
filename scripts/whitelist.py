import os
import sys
import config
import certifi
from common import utils
from pymongo import MongoClient


"""
Configuration
"""

# either USERNAME or USER_ID needs to be specified
USER_ID = 0
USERNAME = ""

NEW_LIMIT = 0

# advanced options
OVERRIDE_BLACKLIST = (
    False  # if False, will prevent blacklisted users from being whitelisted
)

client = MongoClient(
    os.getenv("PROD_MONGODB_CONNECTION_STRING"), tlsCAFile=certifi.where()
)
db = client[config.MONGODB_DB]

whitelist_collection = db[config.MONGODB_USER_WHITELIST_COLLECTION]
user_collection = db[config.MONGODB_USER_DATA_COLLECTION]
chat_data_collection = db[config.MONGODB_CHAT_DATA_COLLECTION]
job_data_collection = db[config.MONGODB_JOB_DATA_COLLECTION]


user_info = None
if USER_ID > 0:
    user_info = user_collection.find_one({"user_id": USER_ID, "superseded_at": ""})
elif USERNAME != "":
    user_info = user_collection.find_one({"username": USERNAME, "superseded_at": ""})

if user_info is None:
    print("User not found")
    sys.exit(0)

user_id = user_info.get("user_id")
username = user_info.get("username")
now = utils.now()

if NEW_LIMIT <= 0:
    whitelist_collection.replace_one(
        {"user_id": user_id, "removed_ts": ""},
        {
            "user_id": user_id,
            "username": username,
            "new_limit": NEW_LIMIT,
            "created_ts": now,
            "removed_ts": "",
        },
        upsert=True,
    )
    chat_data_collection.update_many(
        {"created_by": user_id}, {"$set": {"restriction": "", "updated_ts": now}}
    )
    job_data_collection.update_many(
        {"created_by": user_id, "removed_ts": ""},
        {"$set": {"removed_ts": now, "last_update_ts": now}},
    )
    print("Successfully blacklisted user %s" % user_id)
    sys.exit(0)

existing_entry = whitelist_collection.find_one({"user_id": user_id, "removed_ts": ""})
if (
    existing_entry is not None
    and existing_entry.get("new_limit") <= 0
    and not OVERRIDE_BLACKLIST
):
    print("Người dùng đã bị đưa vào danh sách đen trước đó, đang hủy bỏ quá trình đưa vào danh sách trắng")
    sys.exit(0)

if NEW_LIMIT > config.JOB_LIMIT_PER_PERSON:
    whitelist_collection.replace_one(
        {"user_id": user_id, "removed_ts": ""},
        {
            "user_id": user_id,
            "username": username,
            "new_limit": NEW_LIMIT,
            "created_ts": now,
            "removed_ts": "",
        },
        upsert=True,
    )
    print("Người dùng được đưa vào danh sách trắng thành công %s" % user_id)
    sys.exit(0)

if NEW_LIMIT == config.JOB_LIMIT_PER_PERSON:
    whitelist_collection.update_one(
        {"user_id": user_id, "removed_ts": ""}, {"$set": {"removed_ts": now}}
    )
    print("Đã xóa thành công danh sách trắng cho người dùng %s" % user_id)
    sys.exit(0)

# if NEW_LIMIT < config.JOB_LIMIT_PER_PERSON:
print("NEW_LIMIT có được đặt chính xác không?")
sys.exit(0)
