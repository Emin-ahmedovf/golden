from pyrogram import Client
from pyrogram import filters
from Kelime_bot import OWNER_ID
from pyrogram.types import Message
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.tsbm4n6.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["soz"]

@Client.on_message(filters.command("stat") & filters.user(OWNER_ID))
async def kelimeoyun(c:Client, m:Message):
    tt = sum(1 for _ in datam.find())
    kn = sum(1 for _ in datam.find({"qrup":"kanal"}))
    tt=tt-kn
    await m.reply(f"**〽️ Statistika:\n\nℹ️ Toplam User: {tt}\n♻️ Toplam Guruplar: {kn}**")
