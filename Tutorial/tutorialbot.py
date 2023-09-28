import discord
from discord.ext import commands, tasks
from itertools import cycle # Episode 3
from config import TOKEN
import random # Episode 2
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
# status shows up under the bot's username. NEEDS to be a list
clientStatus = cycle(["in 30",
                      "in 25",
                      "in 20",
                      "in 15",
                      "in 10",
                      "in 5",
                      "Error!!!",
                      "rebooting.."])

# await cannot be used without async, but async can be used without await
async def on_ready(): #starts when the bot starts running
    print("Success: Bot is ready to use!")
    change_status.start() # gives the bot an initial status on startup

# giving the bot a status
@tasks.loop(seconds=5) # function occurs at an interval of every 5 seconds
async def change_status():
    await bot.change_presence(activity=discord.Game(next(clientStatus))) # changes the Discord bot's status

# creating "cogs"
async def load():
    for filename in os.listdir("Tutorial\cogs"):
        if filename.endswith(".py"):
            # [:-3] splices the last three characters of the file's name
            # meaning: a function "myCog.py" will just become "myCog"
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")
            
async def main():
    async with bot:
        await on_ready()
        await load()
        await bot.start(TOKEN)
        
asyncio.run(main()) # runs the main function

#Tutorial: https://www.youtube.com/watch?v=x7oBQNcNGeM&list=PLwqYQaS6jxfk_NCetUOyNRDGAf9_kU90n&index=1&pp=iAQB