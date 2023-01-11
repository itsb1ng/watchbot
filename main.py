import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands, tasks
import discord
from twilio.rest import Client

load_dotenv()

token = os.environ['TOKEN']
authKey = os.environ['AUTH']
sid = os.environ['SID']
phoneNumber = os.environ['PHONE_NUMBER']

intents = discord.Intents.all()
bing = commands.Bot(command_prefix='wb!', intents=intents)

PINK_COLOR = 0xC98FFC

def getInfo(call):
    r = requests.get(call)
    return r.json()


client = Client(sid, authKey)
@bing.event
async def on_message(message):
    send = False
    if message.channel.id == 1057507992397938772:
        send = True
        channel = "Essential"
        print("Essentials Hit")
    if send is True:
        message = client.messages.create(
                body=f'There has been a hit in the {channel} hook',
                messaging_service_sid='MG0f08ea8b441972497f6c63a7eabc1b1c',
                to=phoneNumber
            )
        send = False

bing.run(token)
