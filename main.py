import discord
import asyncio

from discord.ext import commands
from discord.ext import tasks

import os
import colorama
import time

jsm = __import__("jsonmanager")
cc = __import__("comparecollections")
gv = __import__("getvendors")


config = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))

bot = commands.Bot(command_prefix= ">")

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
        mods, name = gv.getVendorData(message)
        neededMods = None
        for i in config.load()["usersToCheck"]:
            neededMods = (cc.compareCollections(i, mods))
            user = await bot.fetch_user(int(i[3]))
            await user.send(f"You are missing {', '.join(neededMods)} from {name}")

    await bot.process_commands(message)

@bot.command(description = "Pay someone else a specified amount of money", brief="Pay someone")
async def registerme(ctx, url):
    print("run")
    membershipType = url.split("/")[3]
    destinyMembershipId = url.split("/")[4]
    characterId = url.split("/")[5]
    discordID = str(ctx.author.id)

    users = config.load()["usersToCheck"]
    newUser = [membershipType, destinyMembershipId, characterId, discordID]
    isNewUser = True

    for i, j in enumerate(users):
        if(newUser[3] == j[3]):
            users[i] = newUser
            isNewUser = False
    if(isNewUser):
        users.append(newUser)

    await ctx.send("Added you to the list!")

    newConfig = config.load()

    newConfig["usersToCheck"] = users

    config.save(newConfig)

@bot.command(description = "Pay someone else a specified amount of money", brief="Pay someone")
async def unregisterme(ctx):


    await ctx.send(content="Removed you from the list!")

    discordID = str(ctx.author.id)
    users = config.load()["usersToCheck"]

    for i, j in enumerate(users):
        if(users[i][3] == discordID):
            users.pop(i)

    newConfig = config.load()

    newConfig["usersToCheck"] = users

    config.save(newConfig)





bot.run(config.load()["token"])
