from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.tsbm4n6.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["soz"]

@Client.on_message(filters.command("rating"))
async def ratingsa(c:Client, m:Message):
    metin = """**🏆 Qlobal üzrə Ən yaxşı 20 oyunçu \n**"""
    eklenen = 0
    l=[]
    for i in datam.find():
        try:
            if i["tür"] != "kanal":
                l.append(i)
        except:
            if int(i["puan"]) != 0:
                l.append(i)
    l.sort(reverse = True,key=lambda x: int(x["puan"]))
    for sy, i in enumerate(l[:20], start=1):
        kisi=i["men"]
        puan=i["puan"]
        md=""
        if sy == 1:
            md="1)"
        elif sy == 10:
            md="10)"
        elif sy == 11:
            md="11)"
        elif sy == 12:
            md="12)"
        elif sy == 13:
            md="13)"
        elif sy == 14:
            md="14)"
        elif sy == 15:
            md="15)"
        elif sy == 16:
            md="16)"
        elif sy == 17:
            md="17)"
        elif sy == 18:
            md="18)"
        elif sy == 19:
            md="19)"
        elif sy == 2:
            md="2)"
        elif sy == 20:
            md="20)"
        elif sy == 3:
            md="3)"
        elif sy == 4:
            md="4)"
        elif sy == 5:
            md="5)"
        elif sy == 6:
            md="6)"
        elif sy == 7:
            md="7)"
        elif sy == 8:
            md="8)"
        elif sy == 9:
            md="9)"
        metin += f"\n{md} {kisi}  ➡️   {puan} Xal"
    await c.send_message(m.chat.id, metin)
