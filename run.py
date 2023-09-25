import discord
import logging
from clients.custom_bot_client import CustomBotClient
from cogs.pingpong import PingPong
from config import TOKEN

def main():
    
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = CustomBotClient(
        command_prefix=">>>",
        intents=intents
        )

    bot.add_cog(PingPong(bot))
    
    bot.run(TOKEN)

    handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)

if __name__ == "__main__":
    main()