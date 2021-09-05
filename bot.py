from discord.ext import commands
from discordTogether import DiscordTogether
import os

client = commands.Bot(command_prefix="!")
togetherControl = DiscordTogether(client,debug=True)


@client.command()
async def yt(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

token = os.getenv(key="TOKEN")
client.run(token)