from telegram import ReplyKeyboardRemove, Update
from telegram.constants import ParseMode
from telegram.ext._contexttypes import ContextTypes

delete_success_message = "Yee! Công việc này bây giờ đã không còn nữa."
restrict_success_message = "Hoan hô! Từ bây giờ __bot_ic__ có thể thiết lập tin nhắn định kỳ. Chạy lại lệnh để chuyển đổi cài đặt hạn chế."
timezone_change_success_message = (
    "Yipee! Múi giờ của bạn đã được cập nhật thành UTC__utc_tz__."
)
reset_success_messge = "Yee! Không còn tin nhắn lặp lại trong cuộc trò chuyện này."
jobs_creation_success_message = "Các tin nhắn định kỳ sau đây được tạo, /list để xem tất cả tin nhắn và thông tin chi tiết của chúng:\n"
attribute_change_success_message = "Yipee! Tin nhắn định kỳ của bạn đã được cập nhật thành công.\n\n/list để xem tất cả tin nhắn và thông tin chi tiết của chúng."
sender_change_success_message = "Người gửi cho %s bây giờ là %s. \n\nHãy nhớ thêm %s vào nhóm/kênh với tư cách quản trị viên và bật:\n1. <i>Thay đổi thông tin nhóm/kênh</i> và\n2. <i>Đăng tin nhắn</i>."
sender_reset_success_message = (
    "Người gửi đã được đặt lại về mặc định để trò chuyện. /changesender để đặt người gửi mới."
)


async def send_delete_success_message(update: Update) -> None:
    await update.message.reply_text(
        delete_success_message, reply_markup=ReplyKeyboardRemove()
    )


async def send_reset_success_message(context: ContextTypes, chat_id: int) -> None:
    await context.bot.send_message(chat_id, reset_success_messge)


async def send_restrict_success_message(update: Update, bot_ic: str) -> None:
    await update.message.reply_text(
        restrict_success_message.replace("__bot_ic__", bot_ic)
    )


async def send_timezone_change_success_message(update: Update, utc_tz: str) -> None:
    reply = timezone_change_success_message.replace("__utc_tz__", utc_tz)
    await update.message.reply_text(reply)


async def send_jobs_creation_success_message(
    update: Update, additional_text: str
) -> None:
    await update.message.reply_text(jobs_creation_success_message + additional_text)


async def send_attribute_change_success_message(update: Update) -> None:
    await update.message.reply_text(
        attribute_change_success_message, reply_markup=ReplyKeyboardRemove()
    )


async def send_sender_reset_success_message(update: Update) -> None:
    await update.message.reply_text(
        sender_reset_success_message, reply_markup=ReplyKeyboardRemove()
    )


async def send_sender_change_success_message(
    update: Update, chat_title: str, bot_username: str
) -> None:
    await update.message.reply_text(
        sender_change_success_message % (chat_title, bot_username, bot_username),
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardRemove(),
    )
