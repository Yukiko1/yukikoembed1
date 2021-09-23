import discord, os, asyncio
from discord.ext import commands
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
from discord_slash.utils.manage_commands import create_option

bot = commands.Bot(command_prefix="your prefix", help_command=None)
slash = SlashCommand(bot, sync_commands=True)

emslash = [
  {
    "name" : "title",
    "description" : "content of title",
    "type" : 3,
    "required" : True
  },
  {
    "name" : "description",
    "description" : "content of description",
    "type" : 3,
    "required" : True
  }
]

@bot.event
async def on_ready():
  print("Im now online :D")

@bot.command(aliases=['latency'])
async def ping(ctx):
  embed=discord.Embed(title="Getting latency..", color=0xFFC0CB)
  await ctx.message.delete()
  m1 = await ctx.send(embed=embed)
  await asyncio.sleep(3.25)
  await m1.delete()
  embed=discord.Embed(description=f"My ping is {round(bot.latency * 1000)}ms", color=0xFFC0CB)
  p = await ctx.send(embed=embed)
  await asyncio.sleep(4.5)
  await p.delete()

@slash.slash(name="", description="Show my latency")
async def zacx(ctx):
  embed=discord.Embed(description=f"My ping is {round(bot.latency * 1000)}ms", color=0xFFC0CB)
  p = await ctx.send(embed=embed)

@slash.slash(name="embed", description="Make me send anything you want in embed", options=emslash)
async def zac(ctx : SlashContext, title, description):
  embed=discord.Embed(title=f"{title}", description=f"{description}", color=0xFFC0CB)
  await ctx.send(embed=embed)

token = os.environ.get('TOKEN')
bot.run(token, bot=True)