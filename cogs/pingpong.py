import discord

class PingPong(discord.ext.commands.Cog, name="PingPong Module"):
    def __init__(self, bot):
        self.bot = bot
        
    @discord.ext.commands.command(name="Ping!")
    async def adhoc_play(self, ctx):
        await ctx.send("Pong!")
        
    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel != None:
            await channel.send(f"A wild {member.mention} has appeared!")