import wojakUtil
import discord

from discord.ext import commands

token = open('DISCORD_TOKEN').readline().rstrip()

bot = commands.Bot(command_prefix='!')


@bot.command()
async def wojak(ctx, *args):
    if len(args):
        wojakName = ''
        for arg in args:
            wojakName += '{} '.format(arg)
        wojakName = wojakName.rstrip()
        url, fileName = wojakUtil.getWojak(wojakName)
    else:
        url, fileName = wojakUtil.getRandomWojak()
    embed = discord.Embed()
    embed.set_image(url=url)
    await ctx.send(embed=embed)


bot.run(token)
