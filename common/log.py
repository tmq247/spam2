import logging
from telegram import Update
from typing import Dict, Any, Optional

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)


# bot
def log_new_job_added(update: Update) -> None:
    logger.info(
        '[BOT] Người dùng "%s" đã thêm công việc mới "%s" trong phòng "%s", chat_id=%s',
        update.message.from_user.id,
        update.message.text,
        update.message.chat.title,
        update.message.chat.id,
    )


def log_new_jobs_added(update: Update, jobs_string: str) -> None:
    logger.info(
        '[BOT] Người dùng "%s" đã thêm một số công việc "%s" trong phòng "%s", chat_id=%s',
        update.message.from_user.id,
        jobs_string,
        update.message.chat.title,
        update.message.chat.id,
    )


def log_new_channel_job_added(update: Update) -> None:
    logger.info(
        '[BOT] Người dùng "%s" đã thêm công việc/nội dung mới cho một kênh, chat_id=%s',
        update.message.from_user.id,
        update.message.chat.id,
    )


def log_new_content_added(last_updated_by: str, jobname: str, chat_id: int) -> None:
    msg = '[BOT] Người dùng "%s" đã thêm nội dung tin nhắn mới cho công việc "%s", chat_id=%s'
    logger.info(msg, last_updated_by, jobname, chat_id)


def log_new_channel_jobname_added(entry: Optional[Any]) -> None:
    logger.info(
        '[BOT] Người dùng "%s" đã thêm tên công việc "%s" trong kênh, channel_id=%s, chat_id=%s',
        entry.get("last_updated_by"),
        entry.get("jobname"),
        entry.get("channel_id"),
        entry.get("chat_id"),
    )


def log_bot_updated(user_id: int, bot_data: Dict[str, Any]) -> None:
    msg = '[BOT] Người dùng "%s" đã nâng cấp bot "%s"'
    logger.info(msg, user_id, bot_data.get("username"))


def log_crontab_updated(last_updated_by: str, jobname: str, chat_id: int) -> None:
    msg = '[BOT] Người dùng "%s" đã thêm crontab mới cho công việc "%s", chat_id=%s'
    logger.info(msg, last_updated_by, jobname, chat_id)


def log_job_removed(last_updated_by: str, jobname: str, chat_id: str) -> None:
    msg = '[BOT] Người dùng "%s" đã xóa công việc "%s", chat_id=%s'
    logger.info(msg, last_updated_by, jobname, chat_id)


def log_option_updated(
    updated_fields: Dict[str, Any], option: str, jobname: str, chat_id: int
) -> None:
    logger.info(
        '[BOT] Người dùng "%s" đã cập nhật tùy chọn "%s" thành "%s" cho công việc "%s", chat_id=%s',
        updated_fields["last_updated_by"],
        option,
        updated_fields[option],
        jobname,
        chat_id,
    )


def log_sender_updated(
    user_id: int, prev_sender: str, new_sender: str, chat_id: int
) -> None:
    msg = '[BOT] Người dùng "%s" đã cập nhật người gửi từ "%s" thành "%s", chat_id=%s'
    logger.info(msg, user_id, prev_sender, new_sender, chat_id)


def log_chat_reset(update: Update) -> None:
    logger.info(
        '[BOT] Người dùng đặt lại cuộc trò chuyện "%s", chat_id=%s',
        update.callback_query.from_user.id,
        update.callback_query.message.chat_id,
    )


def log_photo_transferred(
    user_id: int, new_photo_id: int, chat_id: int, status: int
) -> None:
    msg = '[BOT] Người dùng "%s" đã chuyển ảnh "%s", chat_id="%d", status=%d'
    logger.info(msg, user_id, new_photo_id, chat_id, status)


# database
def log_new_entry(jobname: str, chat_id: int) -> None:
    msg = '[DB] Đã tạo công việc mới, jobname="%s", chat_id=%s'
    logger.info(msg, jobname, str(chat_id))


def log_new_chat(chat_id: int, chat_title: str) -> None:
    msg = "[DB] Đã tạo mục trò chuyện mới, chat_id=%s, chat_title=%s"
    logger.info(msg, str(chat_id), chat_title)


def log_new_user(user_id: int, username: str) -> None:
    msg = '[DB] Đã tạo người dùng mới, user_id=%s, username="%s"'
    logger.info(msg, str(user_id), username)


def log_entry_updated(entry: Optional[Any]) -> None:
    msg = '[DB] Mục nhập công việc được cập nhật "%s", chat_id=%s'
    logger.info(msg, entry.get("jobname"), str(entry.get("chat_id")))


def log_chat_entry_updated(
    chat_id: int, updated_field: str, updated_value: str
) -> None:
    msg = '[DB] Đã cập nhật cuộc trò chuyện %s thành "%s", chat_id=%s'
    logger.info(msg, updated_field, updated_value, chat_id)


def log_chats_tz_updated_by_type(
    count: int, user_id: int, chat_type: str, tz_offset: float
) -> None:
    msg = "[DB] Múi giờ được cập nhật hàng loạt cho cuộc trò chuyện %d, chat_type=%s, user_id=%s, new tz_offset=%d"
    logger.info(msg, count, chat_type, user_id, tz_offset)


def log_user_updated(entry: Optional[Any]) -> None:
    msg = '[DB] Người dùng bị thay thế, user_id=%s, field_changed="%s"'
    logger.info(msg, entry.get("user_id"), entry.get("field_changed"))


def log_username_updated(update: Update) -> None:
    msg = "[DB] Tên người dùng đã thay thế, new username=%s, user_id=%s"
    logger.info(msg, update.message.from_user.username, update.message.from_user.id)


def log_firstname_updated(update: Update) -> None:
    logger.info(
        "[DB] Đã thay thế first_name, mới first_name=%s, username=%s, user_id=%s",
        update.message.from_user.first_name,
        update.message.from_user.username,
        update.message.from_user.id,
    )


def log_update_details(result: Optional[Any]) -> None:
    logger.info(
        f"[DB] Cập nhật mongo, matched={result.matched_count}, modified={result.modified_count}",
    )


# api
def log_api_previous_message_deletion(
    chat_id: int, message_id: str, status_code: int
) -> None:
    msg = "[TELEGRAM API] Đã xóa tin nhắn trước đó, response_status=%s, chat_id=%s, message_id=%s"
    logger.info(msg, status_code, chat_id, message_id)


def log_api_send_message(job_id: int, chat_id: int, status_code: int) -> None:
    msg = '[TELEGRAM API] Tin nhắn đã gửi, job_id="%s", chat_id=%s, response_status=%s'
    logger.info(msg, job_id, chat_id, status_code)


def log_entry_count(count: int) -> None:
    logger.info("[TELEGRAM API] Đang xử lý %d tin nhắn để gửi lần này...", count)


def log_completion(total_count: int) -> None:
    logger.info("[TELEGRAM API] Xử lý xong %d messages", total_count)


# prometheus
def log_update_prometheus(metric: int, value: float) -> None:
    logger.info(
        f"[PROMETHEUS] Prometheus được cập nhật, metric={metric}, value={value}",
    )


# influx
def log_influx_resp(measurement: str, field: str, value: int) -> None:
    logger.info(
        f"[INFLUX] Đã cập nhật influx, measurement={measurement}, field={field}, value={value}"
    )


# script
def log_update_count(count: int) -> None:
    logger.info("[SCRIPT] Đang xử lý (các) tin nhắn %d để hồi sinh...", count)
