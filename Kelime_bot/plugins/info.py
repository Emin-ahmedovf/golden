from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from datetime import datetime
from Config import Config
import shutil, psutil, traceback, os
from Kelime_bot import *
from random import shuffle
import pymongo
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.tsbm4n6.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["datam1"]
datam=mydatam["salam"]



@Client.on_message(filters.command("info"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**İstifadəçi Məlumatı:**\n"
    out_str += f" ⚡️ __Qrup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 💎 __Yanıtlanan İstifadəçi Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Yanıtlanan İstifadəçi ID__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)

@Client.on_message(filters.command("ping"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\n**Ping: {round(ms)}**")
