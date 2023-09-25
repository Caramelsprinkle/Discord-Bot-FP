import discord
from discord.ext import commands

class PingPong(commands.Cog, name="PingPong Module"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
        
    @commands.Cog.listener()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        await ctx.send(f"Pong! {bot_latency} ms.")

async def setup(bot):
        await bot.add_cog(PingPong(bot))