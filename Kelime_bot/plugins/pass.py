from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from Kelime_bot.helpers.keyboards import *
from Kelime_bot.helpers.kelimeler import kelime_sec
from Kelime_bot import *



@Client.on_message(filters.command("kec") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun

    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["pass"] < 5:
            oyun[m.chat.id]["pass"] += 1
            await c.send_message(m.chat.id,f"📖 Yalniz 5 Keçmə Haqqiniz var !\n🥳 Söz keçildi!\n\n✏️ Düzgün Söz : **<code>{oyun[m.chat.id]['kelime']}</code>**")

            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True

            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)

            kelime_list = "".join(f"{harf} " for harf in kelime)
            text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandiracaq Xal : 1
🔎 İpucu 1. Hərf : {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {len(kelime_list) // 2} 

✏️ Qarişiq Hərflərdən Düzgün Sözü Tapin 🥳 
            """
            await c.send_message(m.chat.id, text)

        else:
            await c.send_message(m.chat.id, f"<code>💭 Bağışlayın Keçmək Haqqiniz Bitib !  </code>\n• Oyunu Dayandirmaq üçün /stop Yazin ✍🏻")
    else:
        await m.reply(f"💭 Hazırda qrupda aktiv oyun yoxdur !\n\n• Yeni Oyuna Başlamaq üçün /sgame Yazin ✍🏻")
