import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count+1)
        await ctx.send(f"{count} message(s) have been cleared")
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, modReason):
        await ctx.guild.kick(member)
        kickEmbed = discord.Embed(title="Get Outta Here!",
                                  color=discord.Color.blurple())
        kickEmbed.add_field(name="Kicked:",
                            value=f"{member.name} has been kicked from the server!\n Responsible moderator: {ctx.author.mention}",
                            inline=False)
        kickEmbed.add_field(name="Reason:", value=modReason, inline=False)
        
        await ctx.send(kickEmbed)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, modReason):
        await ctx.guild.ban(member)
        banEmbed = discord.Embed(title="Get Outta Here!",
                                  color=discord.Color.red())
        banEmbed.add_field(name="Ban:",
                            value=f"{member.name} has been **Banned** from the server!\n Responsible moderator: {ctx.author.mention}",
                            inline=False)
        banEmbed.add_field(name="Reason:", value=modReason, inline=False)
        
        await ctx.send(banEmbed)
    
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userID):
        user = discord.Object(id=userID)
        await ctx.guild.unban(user)
        
        unbanEmbed = discord.Embed(title="Get back in Here!",
                                  color=discord.Color.red())
        unbanEmbed.add_field(name="Ban:",
                            value=f"<@{userID}> has been **Unbanned** from the server!\n Responsible moderator: {ctx.author.mention}",
                            inline=False)
        
        await ctx.send(unbanEmbed)
    
async def setup(bot):
    await bot.add_cog(Moderation(bot))