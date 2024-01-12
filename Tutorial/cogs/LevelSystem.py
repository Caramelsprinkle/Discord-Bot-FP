import discord
from discord.ext import commands
import json
import math
import random
import asyncio

class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.save())
        
        with open("Tutorial/cogs/json/users.json", "r") as users:
            self.users = json.load(users)
    
    def levelUp(self, authorID):
        currentExp = self.users[authorID]["experience"]
        currentLevel = self.users[authorID]["level"]
        
        if currentExp >= math.ceil(10 * (currentLevel ** 3)/ 2.5):
            self.users[authorID]["level"] += 1
            return True
        else:
            return False
    
    async def save(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open("Tutorial/cogs/json/users.json", "w") as users:
                json.dump(self.users, users, indent=4)
                
            await asyncio.sleep(5)

    @commands.Cog.listener()
    async def on_ready(self):
        print("LevelSystem is ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        
        authorID = str(message.author.id)
        
        if not authorID in self.users:
            self.users[authorID] = {}
            self.users[authorID]["level"] = 1
            self.users[authorID]["experience"] = 0
        
        randomExperience = random.randint(1, 10)
        self.users[authorID]["experience"] += randomExperience
        
        if self.levelUp(authorID):
            levelUpEmbed = discord.Embed(title="Level Up", color=discord.Color.green())
            levelUpEmbed.add_field(name = "congratulations", value=f"{message.author.mention} has just leveled up to level {self.users[authorID]['level']}")
        
            await message.channel.send(embed=levelUpEmbed)

    @commands.command(aliases = ["rank", "lvl", "r"])
    async def level(self, ctx, user: discord.User=None):
        if user is None:
            user = ctx.author
        else:
            user = user
        
        levelCard = discord.Embed(title=f"{user.name}'s level and experience", color=discord.Color.random())
        levelCard.add_field(name = "level:", value=self.users[str(user.id)]["level"])
        levelCard.add_field(name = "exp:", value=self.users[str(user.id)]["experience"])
        levelCard.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar)
        
        await ctx.send(embed = levelCard)
        
async def setup(bot):
    await bot.add_cog(LevelSystem(bot))       