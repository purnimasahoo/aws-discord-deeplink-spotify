import os
import re
import discord
import pytest
import json
import boto3

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
AWS_REGION = 'your-aws-region'
SNS_TOPIC_ARN = 'your-sns-topic-arn'

@pytest.fixture
def discord_bot():
    client = discord.Client()
    direct_link = None

    sns_client = boto3.client('sns', region_name=AWS_REGION)

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="for Spotify links 🎵"))

    @client.event
    async def on_message(message):
        nonlocal direct_link

        if "open.spotify.com" in message.content:
            protocol, host, kind, identifier, search = re.split(
                "//|/|\?", message.content)

            direct_link = f"spotify://{kind}/{identifier}"
            await message.channel.send(f"Open directly in app: {direct_link}")

            # Publish the direct link to AWS SNS
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=json.dumps({'direct_link': direct_link}),
            )

    client.run(TOKEN)

    yield client, direct_link

    client.close()

def test_spotify_link_response(discord_bot):
    client, direct_link = discord_bot

    # Simulate a user sending a Spotify link
    test_link = "https://open.spotify.com/playlist/3Osa8LTvi4CLYfSpfCdA7v?si=aAC-dNQGRl-CcCJlIWyCfg"
    client.on_message(discord.Message(content=test_link))

    # Check if the direct link is generated as expected
    expected_direct_link = "spotify://playlist/3Osa8LTvi4CLYfSpfCdA7v"
    assert direct_link == expected_direct_link
