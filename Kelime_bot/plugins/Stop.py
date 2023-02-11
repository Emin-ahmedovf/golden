from pyrogram import Client
from pyrogram import filters
from random import shuffle
from Kelime_bot import USERNAME
from Kelime_bot import oyun
from pyrogram.types import Message
from Kelime_bot.helpers.keyboards import *
from Kelime_bot.helpers.kelimeler import kelime_sec
from Kelime_bot import *



@Client.on_message(filters.command("stop"))
async def stop(c:Client, m:Message):
    global oyun

    if m.chat.id not in oyun.keys():
       return await m.reply("Zaten çalışan bir oyun yok.")

    siralama = [
        f"{i} :   {oyun[m.chat.id]['oyuncular'][i]}  Xal"
        for i in oyun[m.chat.id]["oyuncular"]
    ]
    siralama.sort(reverse=False)
    siralama_text = "".join(i + "\n" for i in siralama)
    await c.send_message(m.chat.id, f"{m.from_user.mention} Tərəfindən Dayandirıldı! \n\n Yeni Oyun Başlatmaq üçün \n /sgame Yazın . . .\n\n\n 📝 Xal qazanan Oyunçuların Siyahısı  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
