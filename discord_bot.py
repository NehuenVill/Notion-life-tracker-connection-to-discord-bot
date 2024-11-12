import requests
from dotenv import load_dotenv
import os
from discord.ext import commands
import discord
import datetime

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def add_entry(ctx, name: str, description: str, date: str, emotion: str, picture: str = None):
    try:
        entry_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        await ctx.send("Invalid date format! Please use YYYY-MM-DD.")
        return

    if not picture and ctx.message.attachments:
        picture = ctx.message.attachments[0].url

    embed = discord.Embed(
        title=f"{name}'s Entry",
        description=f"{description}",
        color=discord.Color.blue()
    )

    embed.add_field(name="Date", value=entry_date.strftime("%Y-%m-%d"), inline=False)
    embed.add_field(name="Emotion", value=emotion.capitalize(), inline=False)

    if picture:
        embed.set_image(url=picture)
    embed.set_footer(text=f"Added by {ctx.author}")

    await ctx.send(embed=embed)

bot.run(BOT_TOKEN)