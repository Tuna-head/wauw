import discord
from discord.ext import commands
client = commands.Bot( command_prefix = '^')

@client.event
async def on_ready():
    print('wauw is online.')


@client.event
async def on_message(message):
  if message.content.startswith('wauw') and message.author != client.user:
    channel = message.channel
    await channel.send('wauw')


client.run('NzcwODAwNjA4ODAxNDU2MTU4.X5i2AQ.niARqK2ejfCRnZPzdy0-PEj10SQ')