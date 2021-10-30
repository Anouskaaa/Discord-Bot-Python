import discord
import os
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
import random
import string
import requests
import time
from PIL import Image

bot = commands.Bot(command_prefix="c!")

@bot.event
async def on_ready():
    print(f"Hello Im {bot.user}")

@bot.command()
async def helps(ctx):
    embed = discord.Embed(title="Help", color=0x00ff00)
    embed.add_field(name="Pillow", value="png2jpg, jpg2png, rgb2white, png2webp, webp2png, jpg2webp, webp2jpg", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def png2jpg(ctx):
    await ctx.send("Processing!")
    await ctx.message.attachments[0].save('convert.png')
    im = Image.open("convert.png")
    rgb_im = im.convert('RGB')
    rgb_im.save('converted.jpg', "jpg")
    await ctx.reply("Here your jpg", file=discord.File("converted.jpg"))
    await ctx.send("Thanks For Using Our Service")

@bot.command()
async def jpg2png(ctx):
    await ctx.send("Processing")
    await ctx.message.attachments[0].save("convertjpg.jpg")
    im = Image.open("convertjpg.jpg")
    rgb_im = im.convert('RGB')
    rgb_im.save('convertpng.png', "png")
    await ctx.reply("Here your png", file=discord.File("convertpng.png"))
    await ctx.send("Thanks For Using Our Service")


@bot.command()
async def rgb2white(ctx):
    await ctx.send("Processing!")
    await ctx.message.attachments[0].save("rgb.jpg")
    im = Image.open("rgb.jpg")
    white = im.convert("L")
    white.save("white.jpg", "jpg")
    await ctx.reply("Here you go", file=discord.File("white.jpg"))
    await ctx.send("Thanks For Using Our Service")

@bot.command()
async def png2webp(ctx):
    await ctx.send("Processing!")
    await ctx.message.attachments[0].save("webp.png")
    im = Image.open("webp.png")
    white = im.convert("RGB")
    white.save("webp.webp", "webp")
    await ctx.reply("Here you go", file=discord.File("webp.webp"))
    await ctx.send("Thanks For Using Our Service")

@bot.command()
async def webp2png(ctx):
    await ctx.send("Processing!")
    await ctx.message.attachments[0].save("png.webp")
    im = Image.open("png.webp")
    white = im.convert("RGB")
    white.save("png.png", "png")
    await ctx.reply("Here you go", file=discord.File("png.png"))
    await ctx.send("Thanks For Using Our Service")

@bot.command()
async def jpg2webp(ctx):
    await ctx.send("Processing!")
    await ctx.message.attachments[0].save("webp.jpg")
    im = Image.open("webp.jpg")
    white = im.convert("RGB")
    white.save("webp.webp", "webp")
    await ctx.reply("Here you go", file=discord.File("webp.webp"))
    await ctx.send("Thanks For Using Our Service")

@bot.command()
async def webp2jpg(ctx):
    await ctx.send("Processing!")
    await ctx.message.attachments[0].save("jpg.webp")
    im = Image.open("jpg.webp")
    white = im.convert("RGB")
    white.save("jpg.jpg", "jpg")
    await ctx.reply("Here you go", file=discord.File("jpg.jpg"))
    await ctx.send("Thanks For Using Our Service")





load_dotenv(find_dotenv())
TOKEN = os.getenv("BOT_TOKEN")
bot.run(TOKEN)
