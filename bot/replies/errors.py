from config import JOB_LIMIT_PER_PERSON, BOT_NAME
from telegram import ParseMode, ForceReply

error_message = "Bạn biết điều đó là không đúng..."
exceed_limit_error_message = (
    "Tin nhắn định kỳ hiện chỉ hỗ trợ %d công việc cho mỗi người nhằm nỗ lực giảm thư rác.\n\n__custom_message__Nếu bạn cần tạo nhiều hơn __limit__ công việc, vui lòng liên hệ với chủ sở hữu bot theo địa chỉ @coihaycoc và chỉ định:\n1 . số lượng công việc bạn cần và\n2. tay cầm Telegram của bạn.\n\n<b>Bạn thích bot?</b>\nBạn có thể <a href='@coihaycoc'>mua cà phê cho tôi</a>!"
    % (JOB_LIMIT_PER_PERSON)
)  # html
channels_only_error_message = "Tạo job bằng tin nhắn chuyển tiếp chỉ được kích hoạt cho các kênh. Vui lòng chạy lệnh /add trong __chat_type__ cha của bạnt."
user_unauthorized_error_message = "Ồ không... Bạn không được phép chạy lệnh này. Vui lòng kiểm tra với __bot_ic__ nếu bạn cho rằng đây là lỗi."
wrong_restrction_error_message = (
    "Hạn chế đã được thiết lập. Trước tiên hãy yêu cầu __bot_ic__ bỏ đặt giới hạn bot."
)
timezone_nochange_error_message = "Cái gì? Đó là cùng một múi giờ!"
invalid_new_job_message = "Một công việc có tên này đã tồn tại. Vui lòng /thêm và tạo công việc mới hoặc /chỉnh sửa công việc này."
quiz_unavailable_message = 'Rất tiếc, tin nhắn định kỳ không thể hỗ trợ các câu đố định kỳ trong các kênh và nhóm... vì Telegram không trả về id tùy chọn chính xác cho các tin nhắn được chuyển tiếp (◕︵◕) (<a href="https://docs.python-telegram-bot.org /en/v12.5.1/telegram.poll.html#telegram.Poll. Correct_option_id">xem tài liệu</a>)'
invalid_crontab_message = 'Biểu thức này không hợp lệ. Vui lòng cung cấp một biểu thức hợp lệ. Nhấp vào <a href="https://crontab.guru/">đây</a> nếu bạn cần trợ giúp. Sử dụng /checkcron để kiểm tra biểu thức cron của bạn.'  # html
convo_unauthorized_message = (
    "Chỉ người dùng đã bắt đầu cuộc trò chuyện này mới có thể tiếp tục cuộc trò chuyện này."
)
no_photos_to_delete_error_message = "Không có ảnh để xóa. Kết thúc cuộc trò chuyện..."
attribute_change_error_message = "Đã xảy ra lỗi trên máy chủ... Vui lòng liên hệ với chủ sở hữu bot theo địa chỉ @coihaycoc."
private_only_error_message = "Lệnh này chỉ có thể được chạy trong cuộc trò chuyện riêng tư với %s"
missing_chats_error_message = "Hãy thêm và thiết lập %s vào một nhóm"
missing_bot_in_group_message = "Chấm dứt cuộc trò chuyện... \n\nVui lòng thêm bot vào nhóm với tư cách quản trị viên và bật:\n1. <i>Thay đổi thông tin kênh</i> và\n2. <i>Đăng tin nhắn</i>\ntrước khi chạy /changesender."


def send_error_message(update):
    update.message.reply_text(error_message)


def send_exceed_limit_error_message(update, limit):
    reply_text = exceed_limit_error_message.replace("__limit__", str(limit))
    if limit == JOB_LIMIT_PER_PERSON:
        reply_text = reply_text.replace("__custom_message__", "")
    elif limit < JOB_LIMIT_PER_PERSON:
        reply_text = reply_text.replace(
            "__custom_message__",
            "Tuy nhiên, chúng tôi đã nhận được báo cáo về thư rác từ bạn và kết quả là bạn đã bị đưa vào danh sách đen.\n\n",
        )
    else:
        reply_text = reply_text.replace(
            "__custom_message__",
            "Theo yêu cầu trước đó, chúng tôi đã tăng giới hạn của bạn lên %d.\n\n" % limit,
        )
    update.message.reply_text(
        text=reply_text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


def send_channels_only_error_message(update, chat_type):
    reply = channels_only_error_message.replace("__chat_type__", chat_type)
    update.message.reply_text(reply)


def send_user_unauthorized_error_message(update, bot_ic):
    reply = user_unauthorized_error_message.replace("__bot_ic__", bot_ic)
    update.message.reply_text(reply)


def send_wrong_restriction_message(update, bot_ic):
    reply = wrong_restrction_error_message.replace("__bot_ic__", bot_ic)
    update.message.reply_text(reply)


def send_timezone_nochange_error_message(update):
    update.message.reply_text(timezone_nochange_error_message)


def send_invalid_crontab_message(update):
    update.message.reply_text(
        reply_markup=ForceReply(selective=True),
        text=invalid_crontab_message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


def send_invalid_new_job_message(update):
    update.message.reply_text(invalid_new_job_message)


def send_quiz_unavailable_message(update):
    update.message.reply_text(
        text=quiz_unavailable_message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


def send_no_photos_to_delete_error_message(update):
    update.message.reply_text(no_photos_to_delete_error_message)


def send_attribute_change_error_message(update):
    update.message.reply_text(attribute_change_error_message)


def send_private_only_error_message(update):
    update.message.reply_text(private_only_error_message % BOT_NAME)


def send_missing_chats_error_message(update):
    update.message.reply_text(missing_chats_error_message % BOT_NAME)


def send_missing_bot_in_group_message(update):
    update.message.reply_text(missing_bot_in_group_message, parse_mode=ParseMode.HTML)
