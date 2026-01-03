from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIPMUSIC import app
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ᴍᴜsɪᴄ™ ˼ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ʀᴀᴅʜᴇ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ •
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ʀᴀᴅʜᴇ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ʀᴀᴅʜᴇ ʀᴀᴅʜᴇ •
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/RADHE_MUSIC_ROBOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/BOT_SUPPORTGROUP"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/ll_RADHE7_ll"),
          ],
               [
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/ll_BOTCHAMBER_ll"),

],
[
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/RADHE_MUSIC_ROBOT"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/vip_music_vc_bot"),
              ],
              [
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/RishuXmusicXbot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://t.me/KhushiXchatbot"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://t.me/RishuStringBot"),
InlineKeyboardButton("𝗖𝗔𝗠𝗘𝗥𝗔 𝗛𝗔𝗖𝗞", url=f"https://t.me/RISHU_CAMERA_ROBOT"),
],
[
              InlineKeyboardButton("𝗣𝗛𝗜𝗦𝗛𝗜𝗡𝗚 𝗕𝗢𝗧", url=f"https://t.me/Rishabh_hackbot"),
              InlineKeyboardButton("𝗙𝗜𝗟𝗘 𝗦𝗛𝗔𝗥𝗜𝗡𝗚", url=f"https://t.me/Share_file_robot"),
              ],
              [
              InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗜𝗡𝗙𝗢", url=f"https://t.me/CHAT_INFO_ROBOT"),
InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘 𝗕𝗢𝗧", url=f"https://t.me/Rishu_movie_bot"),
],
[
InlineKeyboardButton("𝗙𝗢𝗡𝗧 𝗖𝗛𝗔𝗡𝗚𝗘𝗥", url=f"https://t.me/RishuXfrontXbot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗚𝗣𝗧", url=f"https://t.me/Gpt_pro_robot"),
],
[
InlineKeyboardButton("𝗜𝗠𝗔𝗚𝗘 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘𝗥", url=f"https://t.me/Image_generaterbot"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://envs.sh/bJh.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
