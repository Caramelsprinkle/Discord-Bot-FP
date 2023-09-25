from discord.ext import commands

class CustomBotClient(commands.Bot):
    async def on_ready(self):
        botName = self.user.name
        print(f"{botName} bot reporting for duty!")