import discord
from discord.ext import commands, tasks
from itertools import cycle
from config import TOKEN
import random

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

@bot.event
async def on_ready(): #starts when the bot starts running
    print("Success: Bot is ready to use!")
    change_status.start() # gives the bot an initial status on startup

@bot.command() # requires user to type in !ping for the bot to return "Pong!" and latency
async def ping(ctx): # 
    # stores the bot's latency into a variable, scaled to provide latency in ms 
    botLatency = round(bot.latency * 1000)
    await ctx.send(f"Pong!\n{botLatency} ms")
    
@bot.command(aliases=("8ball", "8b", "magicball")) # alias provides different alternatives for how the command can be referred to in Discord
async def magic_eightball(ctx, *, question): # * allows for multiple, unknown parameters to be used 
    # opens the text file "eightball_responses.txt" and interprets it as a list[] in random_responses
    with open("Tutorial/eightball_responses.txt", "r") as magicBallLines:
        random_responses = magicBallLines.readlines()
        response = random.choice(random_responses) # outputs a random string from the list of responses
    
    await ctx.send(response) # the bot sends the randomized response

# giving the bot a status
@tasks.loop(seconds=5) # function occurs at an interval of every 5 seconds
async def change_status():
    await bot.change_presence(activity=discord.Game(next(clientStatus))) # changes the Discord bot's status

bot.run(TOKEN) # command gets run by the bot with the associated token

#Tutorial: https://www.youtube.com/watch?v=x7oBQNcNGeM&list=PLwqYQaS6jxfk_NCetUOyNRDGAf9_kU90n&index=1&pp=iAQB