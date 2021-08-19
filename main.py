import discord
import asyncio
import pafy

from discord.ext import commands
from discord.ext import tasks
import os
import colorama
import time

intents = {}


jsm = __import__("jsonmanager")

jsonmanager = jsm(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))

config = jsonmanager.load()

bot = commands.Bot(command_prefix= config.load()["prefix"], intents=intents)


@tasks.loop(hours=24)
async def remove_score():
    print("Daily Reset")



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Remind demonater to get his mods lol"))
    print("Bot is ready")

@bot.event
async def on_message(ctx):
    if(ctx.message.content.startswith("test")):
        ctx.channel.send("omfg wow")


bot.run(config.load()["token"])
