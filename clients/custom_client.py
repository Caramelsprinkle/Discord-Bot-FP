# import discord

# class CustomClient(discord.Client):
#     async def on_ready(self):
#         print(f"{self.user} is ready!")
    
#     async def on_message(self, msg):
#         msgChannel = msg.channel
#         msgContent = msg.content
#         msgAuthor = msg.author
    
#         if msgAuthor == self.user:
#             return
    
#         if msgContent == "!ping":
#             await msgChannel.send(f"Pong!\n{round(self.latency * 1000)}ms")