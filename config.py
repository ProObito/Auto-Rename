import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") #"") #token

    # database config
    DB_NAME = os.environ.get("DB_NAME","autorename")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/4b306f4b15c23a8f22e58.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1536699044').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "0") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002078245108"))
    
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





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper

