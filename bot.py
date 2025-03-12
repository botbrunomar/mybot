import discord
import random
import os
from os import getenv
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Define the shorthand notation for large numbers
multipliers = {
    'k': 1000,
    'm': 1000000,
    'g': 1000000000,
    't': 1000000000000,
    'p': 1000000000000000,
    'e': 1000000000000000000,
    'z': 1000000000000000000000,
    'y': 1000000000000000000000000
}

# Define the payout structure
payouts = [
    (1, 20, 1, 100000),
    (21, 21, 3, 300000),
    (22, 41, 2, 200000),
    (42, 42, 6, 600000),
    (43, 62, 3, 300000),
    (63, 63, 9, 900000),
    (64, 83, 4, 400000),
    (84, 84, 12, 1200000)
]

# Create a bot instance
bot = commands.Bot(
    command_prefix='!',
    intents=discord.Intents.all()
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def bet(ctx, amount: str):
    # Convert the shorthand notation to an integer
    num, suffix = amount[:-1], amount[-1]
    amount_int = int(num) * multipliers.get(suffix, 1)

    # Generate a random number for the vote
    vote_number = random.randint(1, 84)

    # Find the corresponding payout based on the vote number
    for start, end, multiplier, reward in payouts:
        if start <= vote_number <= end:
            payout = reward
            await ctx.send(f'Vote Number: {vote_number}\nMultiplier: {multiplier}x\nReward: {payout}\n')
            return

bot.run(os.getenv('DISCORD_TOKEN'))
