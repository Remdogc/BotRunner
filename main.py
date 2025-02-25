#import required dependencies
import nextcord
from nextcord.ext import commands
from nextcord.ui import *
import os

#import Bot Token
from apikeys import *



client = commands.Bot(intents = nextcord.Intents.all(), command_prefix = '!')


# load the database as soon as the bot launches
@client.event
async def on_ready():
    print("BotRunner is now ready for use!")
    print("-----------------------------")


initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])


if __name__ == '__main__':
    for extention in initial_extensions:
        client.load_extension(extention)



# dev command to make sure the bot reads information
@client.slash_command()
async def debug(ctx):
    """Debug Command For developer"""

    ID = ctx.user.id
    if (ID == 459529087652724736):
        # await ctx.message.delete()
        await ctx.send("New phone who this?")


client.run(BotRunner)