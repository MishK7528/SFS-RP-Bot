import os
import discord
import Cogs.Other.Planete as Planete
from Cogs.Other.Mission import Mission

TOKEN = os.environ.get('DISCORD_TOKEN')

bot = discord.Bot(debug_guilds=[988710399685840926, 827924843944738817])

extensions = ['Cogs.Other.CogMission','Cogs.CogHelp']
for cog in extensions:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Spam Voyager 3 de /help"))
    print('Logged on as {0}!'.format(bot.user))

bot.run(TOKEN)
