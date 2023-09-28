import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # @commands.Cog.listener() # events must use commands.Cog.listener
    # async def on_ready(self):
    #     print("Ping.py is ready!")
        
    @commands.command() # commands must use commands.command
    async def ping(self, ctx): # According to OOP rules, you must always pass the object first before other parameters for commands
        botLatency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong!\n {botLatency} ms.")

async def setup(bot):
    await bot.add_cog(Ping(bot))