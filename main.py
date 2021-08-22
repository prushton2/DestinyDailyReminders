import discord
import asyncio
import pafy

from discord.ext import commands
from discord.ext import tasks
import os
import colorama
import time




jsm = __import__("jsonmanager")
cc = __import__("comparecollections")
gv = __import__("getvendors")


jsonmanager = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))

config = jsonmanager

bot = commands.Bot(command_prefix= "==")


@tasks.loop(minutes=30)
async def check_inventory():
    print("Daily Reset")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Remind demonater to get his mods lol"))
    print("Bot is ready")

@bot.event
async def on_message(message):

    if(message.channel.id == int(config.load()["Charlemagne-channel-id"])):
        print(gv.getVendorData(message))

    if(message.content.startswith("==gv")):
        user = config.load()["usersToCheck"][0]
        print("---------")
        print(gv.getVendorData(user[0],user[1],user[2]))


bot.run(config.load()["token"])
