import discord
from discord.ext import commands
# import asyncio
# import os
# import logging
# from clients.custom_bot_client import CustomBotClient
# from cogs.PingPong import PingPong
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True



# def main():

#     bot = CustomBotClient(
#         command_prefix="$",
#         intents=intents
#         )

#     bot.add_cog(PingPong(bot))

#     bot.run(TOKEN)

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

# if __name__ == "__main__":
#     main()