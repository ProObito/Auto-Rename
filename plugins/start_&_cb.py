import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery, Message, InputMediaPhoto

from helper.database import madflixbotz
from config import Config, Txt 

cc_pic = "https://telegra.ph/file/d25921e2fd894726fe816.jpg"
ar_pic = "https://telegra.ph/file/c3af5e173ae29276a4d59.jpg"
ct_pic = "https://telegra.ph/file/926bee6a49224c7293a54.jpg"

PICS = ('https://telegra.ph/file/26a70cb22a9c2e8b60f5b.jpg https://telegra.ph/file/d04c83b8ddbd23b8585df.jpg https://telegra.ph/file/7f04ff0295d2e5e372da0.jpg https://telegra.ph/file/8f8d34d4e9a8ce07a00a6.jpg https://telegra.ph/file/d2832436c9b74a3a99b84.jpg https://telegra.ph/file/d4d61f9ab0cdb59370851.jpg https://telegra.ph/file/aaf21010cf76cf50d9d79.jpg https://telegra.ph/file/1dc82e7cec650bf15ddc6.jpg https://telegra.ph/file/11a0637a7fc6bc3c8a94b.jpg https://telegra.ph/file/cb0b5f704c236fd06727f.jpg https://telegra.ph/file/9bd6940b929bc64967e06.jpg https://telegra.ph/file/f4d1b8ef56a0f1e75e39c.jpg https://telegra.ph/file/7ada0b833a54f7fcf239d.jpg https://telegra.ph/file/1738cec2f49acd3882461.jpg https://telegra.ph/file/8b506dcbaecf9b3c7885d.jpg https://telegra.ph/file/b9d6b7b50c52c4ba03e9c.jpg').split()

@Client.on_message(filters.private & filters.command("autoconfig"))
async def autoconfig(client, message):
	msg = await message.reply_text("**𝖯𝗅𝖾𝖺𝗌𝖾 𝖶𝖺𝗂𝗍 ....**")
	button = [[InlineKeyboardButton("Instruction for Set Format ❗", callback_data="setformat")],[InlineKeyboardButton("✖️ Cʟᴏsᴇ Mᴇssᴀɢᴇ ✖️", callback_data="close")]]
	user_id = message.from_user.id
	ff, mp, cc, ct, thumb_pic='', '', '', '', ''
	file_format = await madflixbotz.get_format_template(user_id)
	media_pref = await madflixbotz.get_media_preference(user_id)
	caption = await madflixbotz.get_caption(user_id)
	thumb = await madflixbotz.get_thumbnail(user_id)
	
	if file_format:
		ff=file_format
	else:
		ff="None ❌"
		
	if media_pref == 'document':
		mp=f"`{media_pref}` 🗂️"
	elif media_pref == 'video':
		mp=f"`{media_pref}` 📺"
	elif media_pref == 'audio':
		mp=f"`{media_pref}` 🎵"
	else:
		mp="Default⚡"

	if caption:
		cc=caption
	else:
		cc="Default⚡"

	if thumb:
		thumb_pic = thumb
		ct = "Available ✅"
	else:
		thumb_pic = "https://telegra.ph/file/200876e84abfc96bf7394.jpg"
		ct = "None ❌"
		
	output = f"""<b>⚙️ 𝖠𝖴𝖳𝖮 𝖱𝖤𝖭𝖠𝖬𝖤 𝖢𝖮𝖭𝖥𝖨𝖦𝖴𝖱𝖠𝖳𝖨𝖮𝖭 ⚙️</b>
 
<blockquote><b>1. Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ:</b> {ct}</blockquote>
<blockquote><b>2. Cᴜʀʀᴇɴᴛ Aᴜᴛᴏ Fᴏʀᴍᴀᴛ:</b>
➪ {ff}</blockquote>
<blockquote><b>3. Cᴜʀʀᴇɴᴛ Mᴇᴅɪᴀ Oᴜᴛᴘᴜᴛ Fᴏʀᴍᴀᴛ:</b>
➪ {mp}</blockquote>
<blockquote><b>4. Cᴜʀʀᴇɴᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ:</b>
➪ {cc}</blockquote>"""

	await msg.delete()
	if thumb_pic==thumb:
		await message.reply_photo(photo=thumb_pic, caption=output, reply_markup=InlineKeyboardMarkup(button))
	else:
		await message.reply(text=output, reply_markup=InlineKeyboardMarkup(button))
	
@Client.on_message(filters.private & filters.command("help"))
async def help_menu(client, message):
	button = [[InlineKeyboardButton("❕ 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨  ⁉️", callback_data="help")]]
	await message.reply_text("<blockquote>**➪ Click below Button for help**</blockquote>",reply_markup=InlineKeyboardMarkup(button))

@Client.on_message(filters.private & filters.command("cmd"))
async def bot_command(client, message):
	text = """**🤖  𝗕𝗢𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦  🌀**
 
**➪ Cʟɪᴄᴋ ᴛʜᴇ Bᴜᴛᴛᴏɴs Bᴇʟᴏᴡ :**
<blockquote>**1. 𝖭𝗈𝗋𝗆𝖺𝗅 𝖴𝗌𝖾𝗋:** All users can use this.
**2. 𝖠𝖽𝗆𝗂𝗇𝗌:** Only bot admin can use this.</blockquote>"""
	
	button = [[InlineKeyboardButton("𝖭𝗈𝗋𝗆𝖺𝗅 𝖴𝗌𝖾𝗋", callback_data= "nuser"), InlineKeyboardButton("𝖠𝖽𝗆𝗂𝗇𝗌", callback_data="auser")]]
	await message.reply(text=text, reply_markup=InlineKeyboardMarkup(button))

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await madflixbotz.add_user(client, message)                
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton('🤖 Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('❗ Hᴇʟᴩ', callback_data='help')]
    ])
    #if Config.START_PIC:
        #await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    #else:
        #await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)   
    await message.reply_photo(photo=random.choice(PICS), caption=Txt.START_TXT.format(user.mention), reply_markup=button)

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    user_id = query.from_user.id
    if data == "start":
        await query.edit_message_media(
 	        InputMediaPhoto(random.choice(PICS), Txt.START_TXT.format(query.from_user.mention)),
            #disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('🤖 Aʙᴏᴜᴛ', callback_data='about'),
                 InlineKeyboardButton('❗ Hᴇʟᴩ', callback_data='help')]
            ])
        )
    elif data == "help":
        await query.edit_message_media(
            InputMediaPhoto('https://graph.org//file/10f310dd6a7cb56ad7c0b.jpg', caption=Txt.HELP_TXT),
            #disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🌌 𝖳𝖧𝖴𝖬𝖡𝖭𝖠𝖨𝖫", callback_data="st"), InlineKeyboardButton("📑 𝖢𝖠𝖯𝖳𝖨𝖮𝖭𝖲", callback_data="cc")],
		        #[InlineKeyboardButton("📑 𝖢𝖠𝖯𝖳𝖨𝖮𝖭𝖲", callback_data="cc")],
		        [InlineKeyboardButton("✏️ 𝖠𝖴𝖳𝖮 𝖱𝖤𝖭𝖠𝖬𝖤", callback_data="rf")],
                [InlineKeyboardButton("⛔️ Close", callback_data = "close"),
                InlineKeyboardButton("◀️ Back", callback_data = "start")]
            ])            
        ) 
    elif data == "about":
        await query.edit_message_media(
            InputMediaPhoto('https://telegra.ph/file/ff8fbe7d67a3c7492c353.jpg', caption=Txt.ABOUT_TXT.format(client.mention)),
            #disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                #[InlineKeyboardButton("🤖 More Bots", url="https://t.me/Madflix_Bots/7")],
                [InlineKeyboardButton("⛔️ Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")]
            ])            
        ) 
    elif data == "st":
	    await query.edit_message_media(
		    InputMediaPhoto(ct_pic, caption=Txt.THUMBNAIL_TXT),
		    #disable_web_page_preview=True,
		    reply_markup=InlineKeyboardMarkup([
			    #[InlineKeyboardButton('🌌 HOW TO SET THUMBNILE', callback_data='st')],
			    [InlineKeyboardButton("📑 𝖢𝖠𝖯𝖳𝖨𝖮𝖭𝖲", callback_data="cc"), InlineKeyboardButton("✏️ 𝖠𝖴𝖳𝖮 𝖱𝖤𝖭𝖠𝖬𝖤", callback_data="rf")],
			    #[InlineKeyboardButton("✏️ 𝖱𝖤𝖭𝖠𝖬𝖤 𝖥𝖨𝖫𝖤", callback_data="rf")],
			    [InlineKeyboardButton("⛔️ Cʟᴏꜱᴇ", callback_data="close"),InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data="help")]
		    ])
	    ) 
    elif data == "cc":
	    await query.edit_message_media(
		    InputMediaPhoto(cc_pic, caption=Txt.CAPTION_TXT),
		    #disable_web_page_preview=True,
		    reply_markup=InlineKeyboardMarkup([
			    [InlineKeyboardButton('🌌 𝖳𝖧𝖴𝖬𝖡𝖭𝖠𝖨𝖫', callback_data='st'), InlineKeyboardButton("✏️ 𝖠𝖴𝖳𝖮 𝖱𝖤𝖭𝖠𝖬𝖤", callback_data="rf")],
			    #[InlineKeyboardButton("📑 HOW TO SET CUSTOM CAPTION", callback_data="cc")],
			    #[InlineKeyboardButton("✏️ HOW TO RENAME A FILE", callback_data="rf")],
			    [InlineKeyboardButton("⛔️ Cʟᴏꜱᴇ", callback_data="close"),InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data="help")]
		    ])
	    )    
    elif data == "rf":
	    ft= await madflixbotz.get_format_template(user_id)
	    await query.edit_message_media(
		    InputMediaPhoto(ar_pic, caption=Txt.FILE_NAME_TXT.format(format_template=ft)),
		    #disable_web_page_preview=True,
		    reply_markup=InlineKeyboardMarkup([
			    [InlineKeyboardButton('🌌 𝖳𝖧𝖴𝖬𝖡𝖭𝖠𝖨𝖫', callback_data='st'), InlineKeyboardButton("📑 𝖢𝖠𝖯𝖳𝖨𝖮𝖭𝖲", callback_data="cc")],
			    #[InlineKeyboardButton("📑 HOW TO SET CUSTOM CAPTION", callback_data="cc")],
			    #[InlineKeyboardButton("✏️ HOW TO RENAME A FILE", callback_data="rf")],
			    [InlineKeyboardButton("⛔️ Cʟᴏꜱᴇ", callback_data="close"),InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data="help")]
		    ])
	    )
    elif data == "setformat":
	    display ="""<b>❗If you want to set specif format then:</b>

<blockquote>**1. Send any Photo to add thumbnail.**</blockquote>
<blockquote>**2.** Use **/autorename** - to set auto rename</blockquote>
<blockquote>**3.** Use **/setmedia** - to set output media type</blockquote>
<blockquote>**4.** Use **/set_caption** - to set custom caption</blockquote>"""
	    await query.message.edit_text(
		    text=display,
		    disable_web_page_preview=True,
		    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ Cʟᴏsᴇ Mᴇssᴀɢᴇ ✖️", callback_data="close")]])
	    ) 
	    
    elif data == "nuser":
	    text="""**🚻 𝗡𝗢𝗥𝗠𝗔𝗟 𝗨𝗦𝗘𝗥 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 :**

**<u>USER CONFIGURATION</u> :**
<blockquote>NOTE: Only Authorised user can Rename the files..</blockquote>
<blockquote>**‣ /check_autho -** Check if you are authorised user or not !</blockquote>
<blockquote>**‣ /autoconfig -** See your all renaming Configuration</blockquote>

**<u>AUTO RENAME</u> :**
<blockquote>**‣ /autorename -** Set auto rename format</blockquote>
<blockquote>**‣ /setmedia -** Set output media type</blockquote>

**<u>THUMBNAIL</u> :**
<blockquote>**‣ Send any Photo to add thumbnail.**</blockquote>
<blockquote>**‣ /delthumb -** Delete your thumbnile</blockquote>
<blockquote>**‣ /viewthumb -** View your thumbnile</blockquote>

**<u>CAPTION</u> :**
<blockquote>**‣ /set_caption -** Set a custom caption</blockquote>
<blockquote>**‣ /see_caption -** View your caption</blockquote>
<blockquote>**‣ /del_caption -** Delete your caption</blockquote>

<b><i>Need further help, Conatct: @Shidoteshika1</i></b>
"""
	    button = [[InlineKeyboardButton("🔐 𝖠𝖣𝖬𝖨𝖭𝖨𝖲𝖳𝖱𝖠𝖳𝖮𝖱 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲",callback_data = "auser")],[InlineKeyboardButton("⛔️ Cʟᴏꜱᴇ",callback_data = "close"),InlineKeyboardButton("◀️ Bᴀᴄᴋ",callback_data = "bcmd")]]
	    await query.message.edit_text(text=text, reply_markup=InlineKeyboardMarkup(button))
	    
    elif data == "auser":
	    id = query.from_user.id
	    text = """"<b>🔐 𝗔𝗗𝗠𝗜𝗡𝗜𝗦𝗧𝗥𝗔𝗧𝗢𝗥 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 :</b>
     
<b>🤖 <u>BOT CONFIG.</u> :</b>
<blockquote>**‣ /restart -** To restart the BOT</blockquote>
<blockquote>**‣ /status -** Check BOT status</blockquote>
<blockquote>**‣ /broadcast -** Broadcast messagse to the users</blockquote>
     
<b>🚻 <u>AUTHORISED USER CONFIG.</u> :</b>
<blockquote>**‣ /addautho_user -** Add authorised user id</blockquote>
<blockquote>**‣ /delautho_user -** Delete authorised user id</blockquote>
<blockquote>**‣ /autho_users -** See Authorised user id list</blockquote>
     
<b><i>Need further help, Conatct: @Shidoteshika1</i></b>"""
	    if id in Config.ADMIN:
	            button = [[InlineKeyboardButton("🚻 𝖭𝖮𝖱𝖬𝖠𝖫 𝖴𝖲𝖤𝖱 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲",callback_data = "nuser")],[InlineKeyboardButton("⛔️ Cʟᴏꜱᴇ",callback_data = "close"),InlineKeyboardButton("◀️ Bᴀᴄᴋ",callback_data = "bcmd")]]
	            await query.message.edit_text(text=text, reply_markup=InlineKeyboardMarkup(button))

	    else:
		    await query.answer("❌ You are not Admin", show_alert=True)
		    return

    elif data == "bcmd":
	    text = """**🤖  𝗕𝗢𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦  🌀**
 
**➪ Cʟɪᴄᴋ ᴛʜᴇ Bᴜᴛᴛᴏɴs Bᴇʟᴏᴡ :**
<blockquote>**1. 𝖭𝗈𝗋𝗆𝖺𝗅 𝖴𝗌𝖾𝗋:** All users can use this. 
**2. 𝖠𝖽𝗆𝗂𝗇𝗌:** Only bot admin can use this.</blockquote>"""
	
	    button = [[InlineKeyboardButton("𝖭𝗈𝗋𝗆𝖺𝗅 𝖴𝗌𝖾𝗋", callback_data= "nuser"), InlineKeyboardButton("𝖠𝖽𝗆𝗂𝗇𝗌", callback_data="auser")]]
	    await query.message.edit_text(text=text, reply_markup=InlineKeyboardMarkup(button))
	    
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
