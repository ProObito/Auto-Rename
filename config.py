import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20718334")
    API_HASH  = os.environ.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7365322253:AAGXvtgjXmmPO_Zdm-bBFmNXudxxyxejqRY") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Yato")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://YatoPro:ProYato@cluster0.zeaqrcy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    PORT = os.environ.get("PORT", "5373")

    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/29a3acbbab9de5f45a5fe.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6497757690').split()]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'codeflix_bots').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001868871195"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1001868871195"))
    OWNER_ID = int(os.environ.get("OWNER_ID", "6497757690"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))

class Txt(object):
    # part of text configuration
        
    START_TXT = """<b>Hᴇʟʟᴏ {} 👋,

Tʜɪs ɪs ᴀɴ Aᴜᴛᴏ Rᴇɴᴀᴍᴇ ʙᴏᴛ.
<blockquote>ɴᴏᴛᴇ: ᴛʜɪs ʙᴏᴛ ᴅᴏᴇsɴ'ᴛ sᴜᴘᴘᴏʀᴛ ɴᴏʀᴍᴀʟ ғɪʟᴇ ʀᴇɴᴀᴍɪɴɢ</blockquote>

Cʟɪᴄᴋ ᴛʜᴇ Aʙᴏᴜᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ Kɴᴏᴡ ᴍᴏʀᴇ</b>"""

    
    FILE_NAME_TXT = """✏️ <b><u>SETUP AUTO RENAME FORMAT</u></b>

<b>Use below Keywords To Setup Custom File Name</b>
<blockquote>‣ <code>episode</code> -> Replace Episode Number
‣ <code>quality</code> -> Replace Video Resolution</blockquote>
<blockquote><b>Example:-</b> <code>/autorename Eepisode Solo Leveling (quality) ESUB 🜲</code>

<b>➪ Yᴏᴜʀ ᴄᴜʀʀᴇɴᴛ Aᴜᴛᴏ Fᴏʀᴍᴀᴛ:</b> <code>{format_template}</code></blockquote>

<blockquote><b><u>NOTE</u> :</b>\nuse <b>/setmedia</b> command to get desired output format
‣ ᴇxᴀᴍᴘʟᴇ 1: <code>/setmedia document</code> (to get file format output)
‣ ᴇxᴀᴍᴘʟᴇ 2: <code>/setmedia video</code> (to get video format output)
‣ ᴇxᴀᴍᴘʟᴇ 3: <code>/setmedia audio</code> (to get audio format output)</blockquote>"""
    
    ABOUT_TXT = """
<b><blockquote>🤖 Mʏ ɴᴀᴍᴇ: {}</blockquote>

➪ Fɪʟᴇ Oᴘᴇʀᴀᴛɪᴏɴ ᴄᴀɴ ᴅᴏɴᴇ ᴜᴘᴛᴏ 2GB
➪ Bʏ ᴜsɪɴɢ ᴍᴇ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ, Cᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ғɪʟᴇ & ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ, Sᴜᴘᴘᴏʀᴛs ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴀᴘᴛɪᴏɴ.</b>
<blockquote>**ɴᴏᴛᴇ: ᴛʜɪs ʙᴏᴛ ᴅᴏᴇsɴ'ᴛ sᴜᴘᴘᴏʀᴛ ɴᴏʀᴍᴀʟ ғɪʟᴇ ʀᴇɴᴀᴍɪɴɢ**</blockquote>

<b>👾 Developer: @Shidoteshika1</b>"""


    
    THUMBNAIL_TXT = """🌌 <b><u>HOW TO SET THUMBNILE</u></b>

<blockquote>**‣ /start** the BOT and send any photo to automatically set thumbnile</blockquote>
<blockquote>**‣ /delthumb -** Delete your old thumbnile</blockquote>
<blockquote>**‣ /viewthumb -** View your current thumbnile</blockquote>"""    
    
#⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
#⦿ /viewthumb - Use This Command To See Your Thumbnail
#⦿ /delthumb - Use This Command To Delete Your Thumbnail

    CAPTION_TXT = """📑 <b><u>HOW TO SET CUSTOM CAPTION</u></b>

<blockquote>**‣ /set_caption -** Set a custom caption</blockquote>
<blockquote>**‣ /see_caption -** View your caption</blockquote>
<blockquote>**‣ /del_caption -** Delete your caption</blockquote>
<blockquote>**Example:-** `/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`</blockquote>"""
    #<b><u>📝  HOW TO SET CAPTION</u></b>
    
#⦿ /set_caption - Use This Command To Set Your Caption
#⦿ /see_caption - Use This Command To See Your Caption
#⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>
⌬ {0}%
<blockquote>‣ 🗂️ Sɪᴢᴇ: {1} | {2}
‣ 🚀 Sᴩᴇᴇᴅ: {3}/s
‣ ⏰️ Eᴛᴀ: {4}</blockquote></b>
"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>madflixofficial@axl</code> """
    
    HELP_TXT = """<b>
❕ 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨  ⁉️
<blockquote>➪ Hᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ɪᴅᴇᴀ ғᴏʀ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ. Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs ᴀs ᴘᴇʀ Yᴏᴜʀ Nᴇᴇᴅs</blockquote></b>

**If you still don't understand and need further help, Contact - @Shidoteshika1**"""

    SEND_METADATA = """
<b>--Metadata Settings:--</b>

➜ /metadata: Turn on or off metadata.

<b>Description</b> : Metadata will change MKV video files including all audio, streams, and subtitle titles."""

    META_TXT = """
**ᴍᴀɴᴀɢɪɴɢ ᴍᴇᴛᴀᴅᴀᴛᴀ ғᴏʀ ʏᴏᴜʀ ᴠɪᴅᴇᴏs ᴀɴᴅ ғɪʟᴇs**

**ᴠᴀʀɪᴏᴜꜱ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

- **ᴛɪᴛʟᴇ**: Descriptive title of the media.
- **ᴀᴜᴛʜᴏʀ**: The creator or owner of the media.
- **ᴀʀᴛɪꜱᴛ**: The artist associated with the media.
- **ᴀᴜᴅɪᴏ**: Title or description of audio content.
- **ꜱᴜʙᴛɪᴛʟᴇ**: Title of subtitle content.
- **ᴠɪᴅᴇᴏ**: Title or description of video content.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ:**
➜ /metadata: Turn on or off metadata.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ꜱᴇᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

➜ /settitle: Set a custom title of media.
➜ /setauthor: Set the author.
➜ /setartist: Set the artist.
➜ /setaudio: Set audio title.
➜ /setsubtitle: Set subtitle title.
➜ /setvideo: Set video title.

**ᴇxᴀᴍᴘʟᴇ:** /settitle Your Title Here

**ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴇɴʀɪᴄʜ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴡɪᴛʜ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴍᴇᴛᴀᴅᴀᴛᴀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ!**
"""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
