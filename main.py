import discord
import asyncio
import pafy

from discord.ext import commands
from discord.ext import tasks
import os
import colorama
import time


intents = discord.Intents.default() #Gotta setup intents so I can get a member list. Discord requires this for privacy or something, its weird
intents.members = True

def getRoleByName(ctx, name): #Turns a role name into a role ID
    allServerRoles = ctx.guild.roles
    for i in allServerRoles:
        if(i.name.lower() == name.lower()):
            return i

def fetchMemberFromId(ctx, id):
    member = ctx.guild.get_member(id)
    return(member)


pyc = __import__("pyconfig")
jsm = __import__("jsonmanager")
ud  = __import__("userData")
lookupUser = __import__("lookupUser")

config = jsm.JsonManager(pyc.configPath)

bot = commands.Bot(command_prefix= config.load()["prefix"], intents=intents)

commandJsonClass = jsm.JsonManager(pyc.commandsPath)
userData = ud.UserDataClass(pyc.userDataPath, None, bot)

allGroups = []
commandNames = []

tempcommandJson = commandJsonClass.load() #This is me being lazy. Aything with "temp" in it wont be used after like 20 lines at most
tempcommandJson = tempcommandJson['commands']

userData.updateFileFormat() #This makes my life SO MUCH EASIER. It automatically updates the format of the userActivity file so I DONT HAVE TO. THAT FILE IS GIANT! 

needRoleUpdate = True

for key in tempcommandJson: #Should probably rework this. This prevents users adding a whole command without rebooting the bot. Users can modify commands and see them change live, but not add or remove. Low priority, but would be nice to improve
    commandNames.append(key)

print(commandNames)

@tasks.loop(hours=24)
async def remove_score():
    print("Daily Reset")
    global needRoleUpdate
    needRoleUpdate = True
    userData.addScore(-.5)
    userData.pruneUsers()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=config.load()["prefix"]+"help"))
    remove_score.start()
    userData.addScore(.5)
    print("Bot is ready")

@bot.event
async def on_message(ctx):    
    ctx.channel.send("omfg wow")
bot.run(config.load()["token"])
