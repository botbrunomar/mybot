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

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!random'):
        random_number = random.randint(1, 100)
        await message.channel.send(f'Your random number is: {random_number}')

client.run(os.getenv('TOKEN'))
