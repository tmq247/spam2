from telegram import ParseMode, ReplyKeyboardRemove

delete_success_message = "Yeah! Công việc này hiện đã không còn."
restrict_success_message = "Yeah! Từ bây giờ __bot_ic__ có thể thiết lập tin nhắn định kỳ. Chạy lại lệnh để chuyển đổi cài đặt hạn chế."
timezone_change_success_message = (
    "Yeah! Múi giờ của bạn đã được cập nhật thành UTC__utc_tz__."
)
reset_success_messge = "Yeah! Không còn tin nhắn lặp lại trong cuộc trò chuyện này."
jobs_creation_success_message = "Các tin nhắn định kỳ sau đây được tạo, /list để xem tất cả các tin nhắn và thông tin chi tiết của chúng:\n"
attribute_change_success_message = "Yeah! Tin nhắn định kỳ của bạn đã được cập nhật thành công.\n\n/list để xem tất cả tin nhắn và thông tin chi tiết của chúng."
sender_change_success_message = "Người gửi cho %s bây giờ là %s. \n\nHãy nhớ thêm %s vào kênh với tư cách quản trị viên và bật:\n1. <i>Thay đổi thông tin kênh</i> và\n2. <i>Đăng tin nhắn</i>."
sender_reset_success_message = (
    "Người gửi đã được đặt lại về mặc định để trò chuyện. /changesender để đặt người gửi mới."
)


def send_delete_success_message(update):
    update.message.reply_text(
        delete_success_message, reply_markup=ReplyKeyboardRemove()
    )


def send_reset_success_message(context, chat_id):
    context.bot.send_message(chat_id, reset_success_messge)


def send_restrict_success_message(update, bot_ic):
    update.message.reply_text(restrict_success_message.replace("__bot_ic__", bot_ic))


def send_timezone_change_success_message(update, utc_tz):
    reply = timezone_change_success_message.replace("__utc_tz__", utc_tz)
    update.message.reply_text(reply)


def send_jobs_creation_success_message(update, additional_text):
    update.message.reply_text(jobs_creation_success_message + additional_text)


def send_attribute_change_success_message(update):
    update.message.reply_text(
        attribute_change_success_message, reply_markup=ReplyKeyboardRemove()
    )


def send_sender_reset_success_message(update):
    update.message.reply_text(
        sender_reset_success_message, reply_markup=ReplyKeyboardRemove()
    )


def send_sender_change_success_message(update, chat_title, bot_username):
    update.message.reply_text(
        sender_change_success_message % (chat_title, bot_username, bot_username),
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardRemove(),
    )
