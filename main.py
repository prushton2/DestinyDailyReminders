import discord
import asyncio
import pafy

from discord.ext import commands
from discord.ext import tasks

from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

import os
import colorama
import time

jsm = __import__("jsonmanager")
cc = __import__("comparecollections")
gv = __import__("getvendors")


config = jsm.JsonManager(os.path.realpath(os.path.join(os.path.dirname(__file__), "config.json")))

bot = commands.Bot(command_prefix= "==")
slash = SlashCommand(bot, sync_commands=True) # Declares slash commands through the client.

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





@slash.slash(name="registerme",
             description="Registers you with the bot",
             options=[
               create_option(
                 name="url",
                 description="Enter the braytech URL",
                 option_type=3,
                 required=False
               )
             ])

async def registerme(ctx, url: str):
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

@slash.slash(name="unregisterme",
             description="Registers you with the bot")

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
