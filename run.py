import discord
import logging
from clients.custom_bot_client import CustomBotClient
from cogs.pingpong import PingPong
from config import TOKEN

def main():
    bot = CustomBotClient(
        command_prefix=">>>",
        intents=intents
        )

    bot.add_cog(PingPong(bot))
    
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

intents = discord.Intents.default()
intents.message_content = True

class CustomClient(discord.Client(intents=intents)):
    async def on_ready(self):
        print(f"{self.user} is ready!")
    
    async def on_message(self, msg):
        msgChannel = msg.channel
        msgContent = msg.content
        msgAuthor = msg.author
    
        if msgAuthor == self.user:
            return
    
        if msgContent == "!ping":
            await msgChannel.send(f"Pong!\n{round(client.latency * 1000)}ms")
        
client = CustomClient
        
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
client.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)

client.run(TOKEN)