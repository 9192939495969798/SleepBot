import discord
from discord.ext import commands
import wikipedia
import random


class Wiki(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.command(name = 'definiton_lookup',
                        aliases = ['search'],
                        help = "Brings up the definition of the metioned keyword.")
    async def wiki(self, ctx, *,question):
        info = wikipedia.summary(question, 1)
        await ctx.send(embed = discord.Embed(title = "{} Pulled Up A Wiki reference regarding {}".format(ctx.author.name,question),
			description = "**{}.*".format(info),
			colour = random.randint(0,0xffffff),
			timestamp=ctx.message.created_at))

    @commands.command(aliases=['advsearch'])
    async def dwiki(self, ctx, *,question):
        info = wikipedia.summary(question, 3)
        await ctx.send(embed = discord.Embed(title = "{} Pulled Up A Wiki reference regarding {}".format(ctx.author.name,question),
			description = "*{}.*".format(info),
			colour = random.randint(0,0xffffff),
			timestamp=ctx.message.created_at))

def setup(client):
    client.add_cog(Wiki(client))
