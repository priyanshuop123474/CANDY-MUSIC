import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4d412495ab546f9062898.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦  ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð»ð±ðððð®ð¬ð¢ð ð§ ðð§ ððð¯ðð¥ð¨ð©ðð ðð² = [ððð¡ðð¬](https://t.me/C_A_N_D_Y_O_P)

ðð«ððð­ð¨ð« :- [ ððð¡ðð¬](https://t.me/C_A_N_D_Y_O_P)
ðð®ð©ð©ð¨ð«ð­ :- [ðð¥ð¢ð¨ð£](https://t.me/DOSTO_KI_ZOPDI)
ð¢ðªð¡ðð¥ :- [ððð¡ðð¬ ](https://t.me/C_A_N_D_Y_O_P)
ðð¨ð®ð«ðð  :- [â¨  ðð¹ð¶ð°ð¸ âï¸ ð¥ð²ð½ð¼ ð](https://t.me/DOSTO_KI_ZOPDI)
ððð§ððð§ :- [ðððð¬](https://t.me/K_I_T_K_A_T)
ðð¡ð¬ :- [ðððð¡](https://t.me/HNYOP)

ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [ððð¡ðð¬](https://t.me/C_A_N_D_Y_O_P)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/DOSTO_KI_ZOPDI")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4d412495ab546f9062898.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://t.me/DOSTO_KI_ZOPDI")
                ]
            ]
        ),
    )
