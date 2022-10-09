import discord
import os
import stuff
from discord.ext import commands

# print(stuff.todaysDay)
# print(stuff.fullthing)
# formattedDay= f"Your first class is {stuff.todaysDay[0]} from 8:55 AM to 10:10 AM. Your second class is from 10:10 AM to 11:20 AM."

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

@bot.event
async def on_ready():
    print("I'm in")
    print(client.user)

@bot.command()
async def getSchedule(ctx):
  await ctx.send(stuff.todaysDay)
  submit=""
  j=1
  while j<len(stuff.todaysDay)+1:
    submit+=f"Your class is {stuff.db[ctx.author][j]}"
  await ctx.send(submit)
  # see if this does anything

@bot.command()
async def get(ctx):
  await ctx.send(stuff.todaysDay)

@bot.command()
async def setSchedule(ctx, arg):
  newArg = arg.split(",")
  i=0
  texty=""
  while i < len(newArg):
    z=i+1
    texty+=f"Your block {i+1} is {newArg[i]}\n"
    update(ctx.author, z.str(), newArg[i])
    i+=1
  await ctx.send(texty)
  

bot.run("MTAyNzc3MjY2OTEzMjgwODI4NA.G5vLH0.Oa7k_oj2Qq4uF1PDAhs5nevAz78qLahTBZH16c")