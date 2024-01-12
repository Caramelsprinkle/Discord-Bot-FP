# Discord Bot Final Project 2023
This will be where I keep my Discord bot final project :>

# Project Report: Algorithm & Programming
## Project Specifications:
Application: Discord bot (w/ discord.py)
Function: An all-purpose general Discord bot; it takes in messages/commands from a Discord server and produces the appropriate output or executes the appropriate functions. Functional commands should include moderation tools and miscellaneous commands should provide entertainment for members of the server. The bot should also be able to store persistent information in a file that can be retrieved from within Discord.

## Solution Design:
1.	General Structure
The code can be broken down into a main file and a cogs folder which contains all of the individual functions that gets loaded by the bot (to prevent cluttering the main file). The main file tutorialbot.py will send instructions to the bot with the specified token and allow it to function for as long as the file is running. 
Sending these instructions may require the program to pause and wait for the servers or for the bot to respond, this was solved using async and await from the module asyncio, and it is used in almost every function call within the file besides helper functions or internal processes. 
Once everything is ready, the file loads all the cog folders containing all other files, each of which containing a single class. The cogs load all the files by selecting the folder directory with the os module an loading all file (extensions) that end with “.py”. side mention: all cogs required a setup function to add it to the bot
Besides loading files through main function, there are also discord.py specific decorators being utilized to perform other checks or functionalities automatically. The on_ready() function is automatically recognized and is run as soon as the bot has fully finished setup; The @bot.tree.command decorator adds a runnable command activated by inputting “/[command name]” in Discord; @tasks.loop decorator reruns the command every specified interval. With these, I am able to check when the bot is ready to run, change its status every 5 seconds, and create commands.
When a command is loaded into the bot, it will not be able to detect it automatically and will require to be bot.tree.sync so that the command may be updated to the list of commands managed by bot.tree.
2.	Moderation Tools
Available moderation tools include the ability to ban users, unban users, kick users, and clear messages from a chat (up to the number of messages specified). These commands require the user to be granted certain permissions to access. 
Ban, unban, and kick provides fields/options for users to include a reason and will create an embed showing the target of the command and their avatar, the moderator responsible for the command, and the reason behind it. 
The clear command is able to purge a channel of its messages and content by the amount specified by the user before it is executed. Finally, a confirmation message will be sent by the bot.
3.	Leveling System
All users in the server are able to obtain ‘experiences’ and ‘levels’ by simply sending messages. It does this by “listening” to the server for every message that gets sent by a member and assigning them a random amount of experience (1 - 10). The experience and levels of each user are stored in a .json file along with the associated user’s ID. When the application is booted up again, the file will retain memory of all users who has ever typed in the server while the bot is active. Leveling up has a formula for the number of experience required before reaching the next level given by 10 x (currentLevel ^ 3) / 2.5 experience at every user level.
Once a user levels up, an embed will pop up in the channel that the user typed their last message before levelling up indicating their new level alongside showing the member’s avatar and username.
4.	Ping Command
It is a simple command where the bot responds with a “Pong” and relays back their server latency in milliseconds.
5.	Magic Ball Command
A command which responds to a user’s question with one of the premade answers retrieved from a given txt file. The bot opens the file and save readlines() to a variable and then selects at random which lines it will use as its response before finally sending it as a message back to the user in the server.
