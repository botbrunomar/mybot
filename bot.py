import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(override=True)

# Initialize the bot
bot = commands.Bot(
    command_prefix='PREFIX',
    intents = discord.Intents.all()
)

# Define the on_ready event
@bot.event
async def on_ready():
    win_numbers = {11, 22, 33, 44, 55, 66, 77, 88, 99}
    if random.randint(1, 100) in win_numbers:
        print('You Win!')
    else:
        print('You Lose!')

# Define a sample command
@bot.command(name='play')
async def play(ctx):
    win_numbers = {11, 22, 33, 44, 55, 66, 77, 88, 99}
    if random.randint(1, 100) in win_numbers:
        await ctx.send('You Win!')
    else:
        await ctx.send('You Lose!')

# Run the bot
if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))