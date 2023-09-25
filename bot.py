import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is ready!")
    
@client.event
async def on_message(msg):
    msgChannel = msg.channel
    msgContent = msg.content
    msgAuthor = msg.author
    
    if msgAuthor == client.user:
        return
    
    if msgContent == "!ping":
        await msgChannel.send(f"Pong!\n{round(client.latency * 1000)}ms")
        
from config import TOKEN
client.run(TOKEN)