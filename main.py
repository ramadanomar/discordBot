# Discord Dependencies:
import discord
from discord.ext import commands
import music
# Other Dependencies:
import os
from dotenv import load_dotenv

# Loads the .env file for the bot
load_dotenv()

# Main Logic
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Adds Commands to bot list
cogs = [music]
for i in range(len(cogs)):
	cogs[i].setup(client)

# Add ENV Variable
client.run(os.environ['DISCORD_BOT_TOKEN'])
