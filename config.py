from os import getenv
from dotenv import load_dotenv

load_dotenv()

""" General config """
# Set ENV to any value to use webhook instead of polling for bot. Must be set in prod environment.
ENV = getenv("ENV")
TZ_OFFSET = 7.0  # (UTC+08:00)
JOB_LIMIT_PER_PERSON = 10
BOT_NAME = "@coihaycocbot"


""" Telegram config """
TELEGRAM_BOT_TOKEN = getenv("6272942112:AAF9Y6U0B2ZyQ2hdsQ9D_ETT8VtlhzXiDO4")
BOTHOST = getenv("BOTHOST")  # only required in prod environment


""" DB config """
MONGODB_CONNECTION_STRING = getenv("mongodb+srv://minhquang24071996:2407@music.jz0q4j9.mongodb.net/?retryWrites=true&w=majority")
MONGODB_DB = "rm_bot"
MONGODB_JOB_DATA_COLLECTION = "job_data"
MONGODB_CHAT_DATA_COLLECTION = "chat_data"
MONGODB_USER_DATA_COLLECTION = "user_data"
MONGODB_BOT_DATA_COLLECTION = "bot_data"
MONGODB_USER_WHITELIST_COLLECTION = "whitelist"
