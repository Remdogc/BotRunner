import nextcord
from nextcord.ext import commands
import os

from apikeys import *

class run(commands.Cog):

    def __init__(self, client):
        self.client = client

    #command
    @nextcord.slash_command()
    async def run(self, ctx, args:str):
        """run another bot"""

        url = bots[args][1]
        token = bots[args][0]

        path = url.split("/")[-1]
        user = url.split("/")[-2]

        os.chdir("bots")

        os.system(f"git clone {url}")

        os.chdir(path)

        os.system(f'git pull {url}')

        with open('apikeys.py', 'w') as file:
            file.write(f'BOTTOKEN = \'{token}\'')

        os.system("python main.py")





def setup(client):
    client.add_cog(run(client))
