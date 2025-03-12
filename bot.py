import os
import discord
import random
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(override=True)

# Initialize the bot
bot = commands.Bot(
    command_prefix='PREFIX',
    intents=discord.Intents.all()
)

# Define the on_ready event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    win_numbers = {11, 22, 33, 44, 55, 66, 77, 88, 99}
    result = 'You Win!' if random.randint(1, 100) in win_numbers else 'You Lose!'
    print(result)

# Run the bot
if __name__ == '__main__':
    try:
        bot.run(os.getenv('TOKEN'))
    except Exception as e:
        print(f'Error occurred: {e}')
