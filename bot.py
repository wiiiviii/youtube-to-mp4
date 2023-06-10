import discord
import yt_dlp
import logging
import os
import time
import subprocess
from discord.ext import commands
from config import BOT_TOKEN, PREFIX

# Set bot intents 
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Configure logging
logging.basicConfig(level=logging.INFO)

# When bot goes onbline 
@bot.event
async def on_ready():
    subprocess.run(["toilet", "-F", "border", "made by wee"])
    print()
    print(f" ↺  ──    loading bot...          ")
    time.sleep(1)    
    print()
    print(f" ￮  ── ⎥  ■■■□□□□□□□□□□□□□□□□□□□□□□   ⎥")
    time.sleep(1)
    print(f" ￮  ── ⎥  ■■■■■■■■□□□□□□□□□□□□□□□□□   ⎥")
    time.sleep(1)
    print(f" ￮  ── ⎥  ■■■■■■■■■■■■■□□□□□□□□□□□□   ⎥")
    time.sleep(1)
    print(f" ￮  ── ⎥  ■■■■■■■■■■■■■■■■■■■■□□□□□   ⎥")
    time.sleep(1) 
    print(f" ￮  ── ⎥  ■■■■■■■■■■■■■■■■■■■■■■■■■   ⎥")
    print()
    time.sleep(1) 
    print(f" ✓  ──   {bot.user} finished loaded ")
    print()

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if 'youtu' in message.content:
        await download_and_send_mp4(message)

    await bot.process_commands(message)

# Shut down bot command
@bot.command(name='exit', aliases=['close', 'shutdown'])
async def shutdown_bot(ctx):
    await ctx.send(":redcross: `shutting down bot`")
    await bot.close()

# Check if bot is online or not 
@bot.command(name='check', aliases=['ping', 'knock'])
async def check_bot(ctx):
    await ctx.send("✅ `bot is responding`")

async def download_and_send_mp4(message):
    url = extract_youtube_url(message.content)

    if url:
        ydl_opts = {
            'outtmpl': '%(title)s [%(id)s].%(ext)s',
            'format': 'bestvideo[height=480][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            logging.info(f"Downloaded file: {filename}")

        if os.path.isfile(filename):
            await message.delete()  # Delete the original message

            mention_user = message.author.mention
            video_title = info.get('title', '')
            output_message = f"`{video_title}` ({mention_user})" 
            await message.channel.send(output_message, file=discord.File(filename, filename=filename))

        else:
            logging.error(f"File not found: {filename}")

def extract_youtube_url(message_content):
    start_index = message_content.index("youtube")
    end_index = message_content.find(" ", start_index)
    if end_index == -1:
        url = message_content[start_index:]
    else:
        url = message_content[start_index:end_index]
    return url.strip()

bot.run(BOT_TOKEN)