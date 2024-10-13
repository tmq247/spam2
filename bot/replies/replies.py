import json
from telegram.constants import ParseMode
from telegram import (
    ForceReply,
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from bot.replies.success import *
from bot.replies.errors import *
from bot.convos import edit
from common.enums import ContentType
from typing import Any, List, Optional, Sequence, Union
from telegram import KeyboardButton

# custom messages
# html
start_message = "<b>Cảm ơn bạn đã sử dụng Tin nhắn định kỳ!</b>\n\nĐể bắt đầu, vui lòng cho tôi biết múi giờ UTC của bạn. Ví dụ: nếu múi giờ của bạn là UTC+08:30, hãy nhập +08:30.\n\n(vuốt sang trái để trả lời tin nhắn này)"
help_message = 'Tôi có thể giúp bạn lên lịch gửi tin nhắn định kỳ bằng cách sử dụng <a href="https://crontab.guru/">cron schedule expressions</a> (phút. Khoảng thời gian 1 phút).\n\n<b>Các lệnh có sẵn</b>\n/add - thêm công việc mới\n/addmultiple - thêm nhiều công việc\n/edit - chỉnh sửa chi tiết công việc\n/list - liệt kê các công việc đang hoạt động\n/delete - xóa một công việc\n/reset - xóa tất cả công việc\n/changetz - chỉnh sửa múi giờ\n/changesender - thay đổi người gửi cho nhóm\n/options - chỉnh sửa quyền cho nhóm\n/checkcron - kiểm tra tính hợp lệ/ý nghĩa của biểu thức cron\n\n<b>Cảm thấy lạc lõng?</b>\nTham khảo của chúng tôi <a href="https://github.com/hsdevelops/cron-telebot/wiki/User-Guide">hướng dẫn sử dụng</a> để biết thêm hướng dẫn sử dụng.\n\n<b>Tìm thấy một lỗi?</b>\nVui lòng liên hệ với chủ sở hữu bot tại <a href="@COIHAYCOC">@COIHAYCOC</a>.\n\n<b>Thưởng thức bot?</b>\nBạn có thể <a href=":like">:like</a>!'  # html
delete_message = "Này, hãy cho tôi biết tên công việc bạn muốn xóa. Nhận /list các công việc có sẵn.\n\n(vuốt sang trái để trả lời tin nhắn này)"
request_jobname_message = (
    "Cho tôi biết tên công việc của bạn\n\n(vuốt sang trái để trả lời tin nhắn này)"
)
# html
request_crontab_message = 'Hãy cho tôi biểu thức lịch trình cron của bạn (ví dụ: 4 5 * * *), nhấp vào <a href="https://crontab.guru/">here</a> nếu bạn cần giúp đỡ. Sử dụng /checkcron để kiểm tra biểu thức cron của bạn.\n\n(vuốt sang trái để trả lời tin nhắn này)'
request_text_message = (
    "Bây giờ hãy cho tôi những gì bạn muốn gửi\n\n(vuốt sang trái để trả lời tin nhắn này)"
)
request_jobs_message = "Trả lời tin nhắn này kèm theo công việc của bạn theo định dạng sau (ví dụ):\n\n0 10 * * 2 Dọn dẹp một bảng\n0 10 * * 4 Kiểm tra lịch\n0 14 * * 5 Kiểm tra cái này cái kia và cái kia\n\n(vuốt sang trái để trả lời tin nhắn này)"
simple_prompt_message = "/add để tạo một công việc mới"
prompt_new_job_message = "Công việc đã có lĩnh vực này. Vui lòng/add và tạo một công việc mới.Nếu bạn muốn ghi đè,/delete công việc và tạo lại."
list_jobs_message = "Chọn công việc bạn quan tâm để tìm hiểu thêm. Các công việc được liệt kê trên bàn phím trả lời.\n\n(vuốt sang trái để trả lời tin nhắn này)"
checkcron_message = "Này, gửi cho tôi biểu thức cron của bạn, tôi sẽ giải mã nó cho bạn.\n\n(vuốt sang trái để trả lời tin nhắn này)"
checkcron_meaning_message = "Được rồi, điều đó có nghĩa là: "
list_options_message_group = "<b>Tùy chọn nhóm</b>\n/adminsonly - hạn chế bot đối với quản trị viên nhóm\n/creatoronly - hạn chế bot cho người dùng đầu tiên\n\n"
add_to_channel_message = "\n\nHãy nhớ thêm SPAM bot vào kênh với tư cách quản trị viên và bật:\n1. <i>Thay đổi thông tin kênh</i> và\n2. <i>Đăng tin nhắn</i>."
change_timezone_message = "Vui lòng cho tôi biết múi giờ UTC mới của bạn.\n\nLưu ý rằng thao tác này sẽ thay đổi múi giờ cho tất cả công việc được thiết lập trong cuộc trò chuyện này.\n\n(vuốt sang trái để trả lời tin nhắn này)"
checkcron_invalid_message = "Được rồi, đó không phải là cron hợp lệ. Nhấp vào <a href='https://crontab.guru/'>here</a> nếu bạn cần giúp đỡ."  # html
reset_confirmation_message = (
    "Thao tác này sẽ xóa tất cả tin nhắn định kỳ được thiết lập trong cuộc trò chuyện này. Xác nhận?"
)

# convo
choose_job_message = (
    "Chọn công việc bạn muốn chỉnh sửa. Các công việc được liệt kê trên bàn phím trả lời."
)
choose_attribute_message = "Bạn muốn thay đổi thuộc tính nào?"
prompt_new_value_message = "Bạn muốn thay đổi nó thành gì?"
choose_chat_message = "Bạn muốn thay đổi người gửi cuộc trò chuyện nào?"
prompt_user_bot_message = "Thao tác này sẽ thay đổi người gửi tin nhắn trong cuộc trò chuyện đã chọn.\n\nVui lòng gửi cho tôi bot token:"
convo_ended_message = "Đang kết thúc cuộc trò chuyện trước đó...\n\n/add một tin nhắn định kỳ khác hoặc /edit một cái hiện có."
reset_photos_confirmation_message = "Thao tác này sẽ xóa TẤT CẢ ảnh cho công việc này. Tiếp tục?"


def prepare_keyboard(
    entries: List[Optional[Any]], field: str = "jobname"
) -> Sequence[Sequence[Union[str, KeyboardButton]]]:
    keyboard = []
    for i, entry in enumerate(entries):
        if i % 2 == 0:
            keyboard.append([entry[field]])
            continue
        keyboard[len(keyboard) - 1].append(entry[field])
    return keyboard


async def send_start_message(update: Update) -> None:
    await update.message.reply_text(
        reply_markup=ForceReply(selective=True),
        text=start_message,
        parse_mode=ParseMode.HTML,
    )


async def send_help_message(update: Update) -> None:
    await update.message.reply_text(
        help_message, parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


async def send_checkcron_message(update: Update) -> None:
    await update.message.reply_text(
        checkcron_message, reply_markup=ForceReply(selective=True)
    )


async def send_request_jobname_message(update: Update) -> None:
    await update.message.reply_text(
        reply_markup=ForceReply(selective=True), text=request_jobname_message
    )


async def send_request_jobs_message(update: Update) -> None:
    await update.message.reply_text(
        reply_markup=ForceReply(selective=True),
        text=request_jobs_message,
        parse_mode=ParseMode.HTML,
    )


async def send_simple_prompt_message(update: Update) -> None:
    await update.message.reply_text(simple_prompt_message)


async def send_delete_message(update: Update, entries: List[Optional[Any]]) -> None:
    keyboard = prepare_keyboard(entries)
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )

    await update.message.reply_text(delete_message, reply_markup=reply_markup)


async def send_list_jobs_message(update: Update, entries: List[Optional[Any]]) -> None:
    keyboard = prepare_keyboard(entries)
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(list_jobs_message, reply_markup=reply_markup)


async def send_choose_job_message(update: Update, entries: List[Optional[Any]]) -> None:
    keyboard = prepare_keyboard(entries)
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(choose_job_message, reply_markup=reply_markup)


async def send_choose_attribute_message(update: Update) -> None:
    keyboard = [edit.attrs[i : i + 2] for i in range(0, len(edit.attrs), 2)]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(choose_attribute_message, reply_markup=reply_markup)


async def send_list_options_message(update: Update) -> None:
    await update.message.reply_text(
        list_options_message_group,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


async def send_reset_confirmation_message(update: Update) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Confirm", callback_data=1),
            InlineKeyboardButton("Cancel", callback_data=0),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        reset_confirmation_message, reply_markup=reply_markup
    )


async def send_job_details(update: Update, entry: Optional[Any], bot_name: str) -> None:
    photo_id = str(entry.get("photo_id", ""))
    content = entry.get("content", "")

    content_type = entry.get("content_type", "")
    if content_type == ContentType.POLL.value:
        content = "(Poll) %s" % json.loads(content).get("question")

    is_paused = entry.get("paused_ts", "") != ""
    reply_text = "<b>Tên công việc</b>: {}\n<b>Cron</b>: {}\n<b>Nội dung</b>: {}\n<b>Photos</b>: {}\n<b>Loại</b>: {}\n<b>Lần chạy tiếp theo</b>: {}\n\n<b>Tùy chọn nâng cao</b>\nXóa trước đó: {}\nNgười gửi: {}\n\n/edit".format(
        entry.get("jobname", ""),
        entry.get("crontab", ""),
        content,
        "no" if photo_id == "" else len(photo_id.split(";")),
        "in-chat" if entry.get("channel_id", "") == "" else "channel",
        "paused" if is_paused else entry.get("user_nextrun_ts", ""),
        "enabled" if entry.get("option_delete_previous", "") != "" else "disabled",
        bot_name,
    )
    await update.message.reply_text(
        reply_text, parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove()
    )


async def send_request_crontab_message(update: Update) -> None:
    await update.message.reply_text(
        reply_markup=ForceReply(selective=True),
        text=request_crontab_message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


async def send_request_text_message(update: Update) -> None:
    await update.message.reply_text(
        reply_markup=ForceReply(selective=True),
        text=request_text_message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


async def send_confirm_message(
    update: Update, entry: Optional[Any], cron_description: str
) -> None:
    content = 'message "%s"' % entry.get("content")
    if entry.get("content_type") == ContentType.POLL.value:
        content = ContentType.POLL.value
    await update.message.reply_text(
        text='Được rồi. Xong. Đã thêm một công việc có tiêu đề "{}". {} của bạn sẽ được gửi {}. {}'.format(
            entry.get("jobname"),
            content,
            cron_description,
            "" if entry.get("channel_id", "") == "" else add_to_channel_message,
        ),
        parse_mode=ParseMode.HTML,
    )


async def send_checkcron_invalid_message(update: Update) -> None:
    await update.message.reply_text(
        text=checkcron_invalid_message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


async def send_checkcron_meaning_message(update: Update, cron_description: str) -> None:
    await update.message.reply_text(checkcron_meaning_message + cron_description)


async def send_prompt_new_job_message(update: Update) -> None:
    await update.message.reply_text(prompt_new_job_message)


async def send_change_timezone_message(update: Update) -> None:
    await update.message.reply_text(
        reply_markup=ForceReply(selective=True), text=change_timezone_message
    )


async def send_convo_ended_message(update: Update) -> None:
    await update.message.reply_text(
        convo_ended_message, reply_markup=ReplyKeyboardRemove()
    )


async def send_prompt_new_value_message(update: Update) -> None:
    await update.message.reply_text(
        prompt_new_value_message,
        reply_markup=ForceReply(selective=True),
    )


async def send_reset_photos_confirmation_message(update: Update) -> None:
    keyboard = [["yes", "no"]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(
        reset_photos_confirmation_message, reply_markup=reply_markup
    )


async def send_prompt_user_bot_message(update: Update) -> None:
    await update.message.reply_text(
        prompt_user_bot_message, reply_markup=ReplyKeyboardRemove()
    )


async def send_choose_chat_message(
    update: Update, entries: List[Optional[Any]]
) -> None:
    keyboard = prepare_keyboard(entries, field="chat_title")
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(choose_chat_message, reply_markup=reply_markup)
