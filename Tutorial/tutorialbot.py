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
botStatus = cycle(["in 30",
                      "in 25",
                      "in 20",
                      "in 15",
                      "in 10",
                      "in 5",
                      "Error!!!",
                      "rebooting.."])

# await cannot be used without async, but async can be used without await
@bot.event
async def on_ready(): #starts when the bot starts running
    await bot.tree.sync()
    print("Success: Bot is ready to use!")
    change_status.start() # gives the bot an initial status on startup
    
@bot.tree.command(name="ping", description="Shows bot's latency")
async def ping(interaction: discord.Interaction):
    # did this to figure out why the command wasn't working initially. Apparently you can't have your app name include "Discord"
    try:
        botLatency = round(bot.latency * 1000)
        await interaction.response.send_message(f"Pong {botLatency} ms")
    except Exception as e:
        print(e)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("You do not have the permissions to execute this command.")

# giving the bot a status
@tasks.loop(seconds=5) # function occurs at an interval of every 5 seconds
async def change_status():
    await bot.change_presence(activity=discord.Game(next(botStatus))) # changes the Discord bot's status

# creating "cogs"
async def load():
    for filename in os.listdir("Tutorial\cogs"):
        if filename.endswith(".py"):
            # [:-3] splices the last three characters of the file's name
            # meaning: a function "myCog.py" will just become "myCog"
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")

class TestMenuButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    try:
        @discord.ui.button(label="Test", style=discord.ButtonStyle.blurple)
        async def test(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.channel.send(content="I've been clicked")
        @discord.ui.button(label="Test", style=discord.ButtonStyle.green)
        async def test1(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.channel.send(content="I've been clicked")
        @discord.ui.button(label="Test", style=discord.ButtonStyle.red)
        async def test2(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.channel.send(content="I've been clicked")
    except Exception as e:
        print(e)

@bot.tree.command(name="buttonmenu")
async def buttonMenu(interaction: discord.Interaction):
    await interaction.response.send_message(content="Here's my button menu", view=TestMenuButton())

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)
        
asyncio.run(main()) # runs the main function

#Tutorial: https://www.youtube.com/watch?v=x7oBQNcNGeM&list=PLwqYQaS6jxfk_NCetUOyNRDGAf9_kU90n&index=1&pp=iAQB