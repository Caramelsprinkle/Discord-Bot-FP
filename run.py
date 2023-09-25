import discord
import logging

intents = discord.Intents.default()
intents.message_content = True

class CustomClient(discord.Client(intents=intents)):
    async def on_ready():
        print(f"{client.user} is ready!")
    
    async def on_message(msg):
        msgChannel = msg.channel
        msgContent = msg.content
        msgAuthor = msg.author
    
        if msgAuthor == client.user:
            return
    
        if msgContent == "!ping":
            await msgChannel.send(f"Pong!\n{round(client.latency * 1000)}ms")
        
client = CustomClient
        
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
client.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)

from config import TOKEN
client.run(TOKEN)