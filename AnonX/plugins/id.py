from pyrogram import Client, filters
from pyrogram.types import Message

from AnonX import app

def get_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@app.on_message(filters.command(["id", "stickerid", "stkid", "stckrid"]))
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>ᴄʜᴀᴛ ɪᴅ</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_id(message.reply_to_message)
        else:
            _id += "<b>ᴜsᴇʀ ɪᴅ</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
      

#bin.py
@app.on_message(filters.command(["bin", "vbin"]))
async def _(m):
    text = m.pattern_match.group(1).strip()
    if len(text) < 6:
        await m.sod("Invalid bin.")
        return
    bin_info = get_bin_info(text[:6])
    if not bin_info:
        await m.sod("Bin not found.", time= 5)
        return
    mess = f"""
<b>Bin</b>: <code>{text[:6]}</code>
<b>Vendor</b>: <b>{bin_info['vendor']}</b>
<b>Type</b>: <b>{bin_info['type']}</b>
<b>Level</b>: <b>{bin_info['level']}</b>
<b>Prepaid</b>: <b>{bin_info['prepaid']}</b>
<b>Bank name</b>: <b>{bin_info['bank_name']}</b>
<b>Iso</b>: <b>{bin_info['iso']} {bin_info['flag']}</b>
<b>Country</b>: <b>{bin_info['country']}</b>
"""
    await m.sod(mess)


