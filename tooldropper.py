# import librerie 
import random
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *

api_id = 1 # inserisci api id
api_hash = " " # inserisci api hahs
tokengenerator = " " # token del bot

generator = Client('tooldropper', api_id, api_hash, bot_token=tokengenerator)
genfile = ["", ""] # mettere i file con estenzione finale esempio "whatsapp.apk"
genfilebtn = InlineKeyboardMarkup([[InlineKeyboardButton("", "gnfile")]]) # mettere il nome inline fra le ""
bot_aggiunto = """ """ # messaggio di aggiunta al gruppo
info = """ """ # inserisci messaggio info
tool_da_generare = ["test", "test2", "test3", "test3"] # inserisci i metodi per andare a capo usa i \n


@generator.on_message(filters.private & filters.command("start"))
async def startabot(client, message):
    await client.send_message(message.chat.id, f""" """, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ GENERA ✨", "gen")]])) # messaggio start

# genera random tool nella lista tool_da_generare
@generator.on_message(filters.command("get"))
async def gettastotool(client, message):
    await message.reply(f"{random.choice(tool_da_generare)}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ GENERA ✨", callback_data="gen")]]), quote=True)

@generator.on_message(filters.command("genfile"))
async def file(client, message):
    await client.send_document(message.chat.id, f"{random.choice(genfile)}", reply_markup=genfilebtn, quote=True)

@generator.on_message(filters.private & filters.command("info"))
async def infodelbot(client, message):
    await message.reply(info, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Menu start", "back")]]))

@generator.on_message(filters.new_chat_members)
async def aggiuntabot(client, message):
    for user in message.new_chat_members:
        if user.is_self:
            await message.reply(bot_aggiunto, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ GENERA ✨", "gen")]]))

@generator.on_callback_query()
async def bottone(client, query):
    if query.data == "gen":
        await client.send_message(query.message.chat.id, f"{random.choice(tool_da_generare)}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ GENERA ✨", "gen")]]))
    elif query.data == "back":
        await query.message.edit(f""" """, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ GENERA ✨", "gen")]])) # rimettere messaggio 
    elif query.data == "gnfile":
        await client.send_document(query.message.chat.id, f"{random.choice(genfile)}", reply_markup=genfilebtn)


# copyright by @ChillatoDev
generator.run()
