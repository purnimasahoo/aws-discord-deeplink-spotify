# bot.py
import os
import re
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

url = "https://open.spotify.com/playlist/3Osa8LTvi4CLYfSpfCdA7v?si=aAC-dNQGRl-CcCJlIWyCfg"


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="for Spotify links 🎵"))


@ client.event
async def on_message(message):
    if "open.spotify.com" in message.content:
        protocol, host, kind, identifier, search = re.split(
            "//|/|\?", message.content)

        directLink = "<spotify://" + kind + "/" + identifier + ">"
        await message.channel.send("Open directly in app: " + directLink)


client.run(TOKEN)
