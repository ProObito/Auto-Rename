from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import madflixbotz

AR ="""✏️ <b><u>SETUP AUTO RENAME FORMAT</u></b>

<b>Use below Keywords To Setup Custom File Name</b>
<blockquote>‣ <code>episode</code> -> Replace Episode Number
‣ <code>quality</code> -> Replace Video Resolution</blockquote>
<blockquote><b>Example:-</b> <code>/autorename Eepisode Solo Leveling (quality) ESUB 🜲</code></blockquote>"""

SM = """<b><u>SET MEDIA TYPE PREFRENCE</u>:</b>

<b>Follow the below examples</b>
<blockquote>‣ ᴇxᴀᴍᴘʟᴇ 1: 
<code>/setmedia document</code> 
(to get file format output)</blockquote>
<blockquote>‣ ᴇxᴀᴍᴘʟᴇ 2: 
<code>/setmedia video</code> 
(to get video format output)</blockquote>
<blockquote>‣ ᴇxᴀᴍᴘʟᴇ 3: 
<code>/setmedia audio</code> 
(to get audio format output)</blockquote>
<blockquote>‣ ᴇxᴀᴍᴘʟᴇ 4: 
<code>/setmedia None</code> 
<code>/setmedia none</code> 
(to set media type as default)</blockquote>"""

button = [[InlineKeyboardButton('⛔️ Cʟᴏsᴇ Mᴇssᴀɢᴇ',callback_data='close')]]

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id
    # Extract the format from the command
    invalid=''
    format_template = message.text.split("/autorename", 1)[1].strip()
    if format_template is invalid:
        await message.reply_text(text=AR, reply_markup=InlineKeyboardMarkup(button))
    else:
        if format_template=="None" or format_template=="none":
            format_template=None
        # Save the format template to the database
        await madflixbotz.set_format_template(user_id, format_template)
        #ft = await madflixbotz.get_format_template(user_id)
        await message.reply_text(f"**Auto Rename Format Updated Successfully! ✅**\n<blockquote><code>{format_template}</code></blockquote>")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()
    fixed = ("document", "video", "audio", "None", "none")

    if media_type=='' or media_type not in fixed:
        await message.reply_text(text=SM, reply_markup=InlineKeyboardMarkup(button))
    else:
        if media_type==fixed[3] or media_type==fixed[4]:
            media_type = None
        # Save the preferred media type to the database
        await madflixbotz.set_media_preference(user_id, media_type)

        await message.reply_text(f"**Media Preference Set To : {media_type}** ✅")






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
