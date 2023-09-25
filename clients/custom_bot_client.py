from discord.ext import commands

class CustomBotClient(commands.Bot):
    async def on_ready(self):
        botName = self.user.name
        print(f"{botName} bot reporting for duty!")
    
    async def on_message(self, msg):
        msgChannel = msg.channel
        msgContent = msg.content
        msgAuthor = msg.author
    
        if msgAuthor == self.user:
            return
    
        if msgContent == "!ping":
            await msgChannel.send(f"Pong!\n{round(self.latency * 1000)}ms")