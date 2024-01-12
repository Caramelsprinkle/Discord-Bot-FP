import discord
from discord.ext import commands
import random

aliases = ("8ball", "8b", "magicball")

class MagicEightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases)
    async def magicEightBall(self, ctx, *, question):
        with open("Tutorial/eightball_responses.txt", "r") as magicBallLines:
            random_responses = magicBallLines.readlines()
            response = random.choice(random_responses)
        
        await ctx.send(response)
        
async def setup(bot):
    await bot.add_cog(MagicEightBall(bot))