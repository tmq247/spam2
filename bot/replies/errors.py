from config import JOB_LIMIT_PER_PERSON, BOT_NAME
from telegram import ForceReply, Update
from telegram.constants import ParseMode

error_message = "Bạn biết điều đó không đúng..."
exceed_limit_error_message = (
    "Recurring Messages currently only supports %d jobs per person, in an effort to reduce spam.\n\n__custom_message__If you need to create more than __limit__ jobs, please contact the bot owner at hs.develops.1@gmail.com specifying:\n1. the number of jobs you need, and\n2. your Telegram handle.\n\n<b>Enjoying the bot?</b>\nYou can <a href='https://www.buymeacoffee.com/rmteam'>buy the RM team a coffee</a>!"
    % (JOB_LIMIT_PER_PERSON)
)  # html
channels_only_error_message = "Tạo việc làm bằng tin nhắn chuyển tiếp chỉ được kích hoạt cho các kênh. Vui lòng chạy lệnh /add trong cuộc trò chuyện __chat_type__ của bạn."
user_unauthorized_error_message = "Ồ không... Bạn không được phép chạy lệnh này. Vui lòng kiểm tra với __bot_ic__ nếu bạn cho rằng đây là lỗi."
wrong_restrction_error_message = (
    "Hạn chế đã được thiết lập. Trước tiên hãy yêu cầu __bot_ic__ bỏ đặt giới hạn bot."
)
timezone_nochange_error_message = "Cái gì? Đó là cùng một múi giờ!"
invalid_new_job_message = "Một công việc có tên này đã tồn tại. Vui lòng /add và tạo công việc mới hoặc /edit công việc này."
quiz_unavailable_message = 'Rất tiếc, tin nhắn định kỳ không thể hỗ trợ các câu đố định kỳ trong các kênh và nhóm... vì Telegram không trả về id tùy chọn chính xác cho các tin nhắn được chuyển tiếp (◕︵◕) (<a href="https://docs.python-telegram-bot.org/en/v12.5.1/telegram.poll.html#telegram.Poll.correct_option_id">see docs</a>)'
invalid_crontab_message = 'Biểu thức này không hợp lệ. Vui lòng cung cấp một biểu thức hợp lệ. Nhấp vào <a href="https://crontab.guru/">here</a> nếu bạn cần giúp đỡ. Sử dụng /checkcron để kiểm tra biểu thức cron của bạn.'  # html
convo_unauthorized_message = (
    "Chỉ người dùng đã bắt đầu cuộc trò chuyện này mới có thể tiếp tục cuộc trò chuyện này."
)
no_photos_to_delete_error_message = "Không có ảnh để xóa. Kết thúc cuộc trò chuyện..."
attribute_change_error_message = "Đã xảy ra lỗi trên máy chủ... Vui lòng liên hệ với chủ sở hữu bot theo địa chỉ @COIHAYCOC."
private_only_error_message = "Lệnh này chỉ có thể được chạy trong cuộc trò chuyện riêng tư với %s"
missing_chats_error_message = "Vui lòng thêm và thiết lập %s trong một nhóm"
missing_bot_in_group_message = "Chấm dứt cuộc trò chuyện... \n\nVui lòng thêm bot vào nhóm với tư cách quản trị viên và kích hoạt:\n1. <i>Change Channel Info</i> và\n2. <i>Post Messages</i>\ntrước khi chạy /changesender."


async def send_error_message(update: Update) -> None:
    await update.message.reply_text(error_message)


async def send_exceed_limit_error_message(update: Update, limit: int) -> None:
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
    await update.message.reply_text(
        text=reply_text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


async def send_channels_only_error_message(update: Update, chat_type: str) -> None:
    reply = channels_only_error_message.replace("__chat_type__", chat_type)
    await update.message.reply_text(reply)


async def send_user_unauthorized_error_message(update: Update, bot_ic: str) -> None:
    reply = user_unauthorized_error_message.replace("__bot_ic__", bot_ic)
    await update.message.reply_text(reply)


async def send_wrong_restriction_message(update: Update, bot_ic: str) -> None:
    reply = wrong_restrction_error_message.replace("__bot_ic__", bot_ic)
    await update.message.reply_text(reply)


async def send_timezone_nochange_error_message(update: Update) -> None:
    await update.message.reply_text(timezone_nochange_error_message)


async def send_invalid_crontab_message(update: Update) -> None:
    await update.message.reply_text(
        reply_markup=ForceReply(selective=True),
        text=invalid_crontab_message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


async def send_invalid_new_job_message(update: Update) -> None:
    await update.message.reply_text(invalid_new_job_message)


async def send_quiz_unavailable_message(update: Update) -> None:
    await update.message.reply_text(
        text=quiz_unavailable_message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


async def send_no_photos_to_delete_error_message(update: Update) -> None:
    await update.message.reply_text(no_photos_to_delete_error_message)


async def send_attribute_change_error_message(update: Update) -> None:
    await update.message.reply_text(attribute_change_error_message)


async def send_private_only_error_message(update: Update) -> None:
    await update.message.reply_text(private_only_error_message % BOT_NAME)


async def send_missing_chats_error_message(update: Update) -> None:
    await update.message.reply_text(missing_chats_error_message % BOT_NAME)


async def send_missing_bot_in_group_message(update: Update) -> None:
    await update.message.reply_text(
        missing_bot_in_group_message, parse_mode=ParseMode.HTML
    )
