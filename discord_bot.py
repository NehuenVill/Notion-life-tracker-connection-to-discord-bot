import requests
from dotenv import load_dotenv
import os
from discord.ext import commands
import discord
from datetime import datetime
import notion
import pytz

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def add(ctx, name: str, description: str, edate: str, emotion: str, picture: str = None):
    
    entry_date = ""
    tz = pytz.timezone('America/Argentina/Buenos_Aires')
    
    try:
        if edate == "":
            entry_date = datetime.now()
            entry_date = tz.localize(entry_date)
            entry_date = entry_date.strftime("%Y-%m-%d")
        else:
            entry_date = datetime.strptime(edate, "%Y-%m-%d")
            entry_date = tz.localize(entry_date)
            entry_date = entry_date.strftime("%Y-%m-%d")
    except ValueError:
        await ctx.send("Invalid date format! Please use YYYY-MM-DD.")
        return

    if not picture and ctx.message.attachments:
        picture = ctx.message.attachments[0].url

    try:

        notion.add_event_to_notion(
        name=name,
        description=description,
        date=entry_date,
        picture_url=picture,
        emotion=emotion.lower(),
        )

        embed = discord.Embed(
            title=f"Entry added successfully",
            description=name,
            color=discord.Color.blue()
            )
            
        embed.add_field(name="Description", value=description, inline=False)
        embed.add_field(name="Date", value=entry_date, inline=False)
        embed.add_field(name="Emotion", value=emotion.capitalize(), inline=False)

        if picture:
            embed.set_image(url=picture)
        embed.set_footer(text=f"Added by {ctx.author}")

        await ctx.send(embed=embed)

    except Exception as e:

        await ctx.send(e)


bot.run(BOT_TOKEN)