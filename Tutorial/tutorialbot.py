import discord
from discord.ext import commands
from config import TOKEN
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready(): #starts when the bot starts running
    print("Success: Bot is ready to use!")

@client.command() # requires user to type in !ping for the bot to return "Pong!" and latency
async def ping(ctx): # 
    # stores the bot's latency into a variable, scaled to provide latency in ms 
    botLatency = round(client.latency * 1000)
    await ctx.send(f"Pong!\n{botLatency} ms")
    
@client.command(aliases=("8ball", "8b", "magicball")) # alias provides different alternatives for how the command can be referred to in Discord
async def magic_eightball(ctx, *, question): # * allows for multiple, unknown parameters to be used 
    # opens the text file "eightball_responses.txt" and interprets it as a list[] in random_responses
    with open("Tutorial/eightball_responses.txt", "r") as magicBallLines:
        random_responses = magicBallLines.readlines()
        response = random.choice(random_responses) # outputs a random string from the list of responses
    
    await ctx.send(response) # the bot sends the randomized response

client.run(TOKEN) # command gets run by the bot with the associated token

#Tutorial: https://www.youtube.com/watch?v=x7oBQNcNGeM&list=PLwqYQaS6jxfk_NCetUOyNRDGAf9_kU90n&index=1&pp=iAQB