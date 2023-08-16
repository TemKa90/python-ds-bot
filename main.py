import discord
from discord.ext import commands
import os, sqlite3


PREFIX = '!'
token = 'MTAyNDI5NDU5MDkzMDUwNTc1OQ.GeSN64.6KWFo1xn5Z9cT4yznsSt6oim52LHSG5LA579rk'

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix = PREFIX, intents = intents)
client.remove_command('help')

#   DataBase
def db_connecting():
    # global base, cursor
    base = sqlite3.connect('DataBase.db')
    cursor = base.cursor()
    return base, cursor

#   Online
@client.event
async def on_ready():
    db_connecting()

from commands import *

#   Connect
client.run(token)