import discord
from discord.ext import commands

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def embed(self, ctx):
        embedMessage = discord.Embed(title="Title of Embed",
                                      description="Description of Embed",
                                      color=ctx.author.color)
        embedMessage.set_author(name=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        embedMessage.add_field(name="Field name", value="Field Value", inline=False)
        embedMessage.set_thumbnail(url=ctx.guild.icon)
        embedMessage.set_image(url=ctx.guild.icon)
        embedMessage.set_footer(text="Footer", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embedMessage)
        
        
async def setup(bot):
    await bot.add_cog(Embed(bot))