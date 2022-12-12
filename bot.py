"""Bot"""
import os
import discord

from discord.ext import commands
from dotenv import load_dotenv
from references import gif_links

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

prefix = commands.when_mentioned_or("mcm ", "mcm")


class Bot(commands.Bot):
    """Prepares bot for use and perform application command (slash command) syncing"""

    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix=prefix,
            case_insensitive=True,
            intents=intents,
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="Serving you",
            ),
        )

    async def on_command_error(self, ctx, error):  # pylint: disable=W0221
        await ctx.reply(error, ephemeral=True)


bot = Bot()


@bot.event
async def on_ready():
    """Executes once the bot is up and running"""
    print(
        f"{discord.version_info}\n" f"{bot.user} is connected to the following guilds:"
    )
    for guild in bot.guilds:
        print(f"* {guild.name} (id: {guild.id})")


@bot.event
async def on_message(message):
    """Actions based on messages read"""
    message.content = message.content.lower()
    if message.author == bot.user:
        return

    if message.content == "hi":
        await message.channel.send(gif_links.hello)

    await bot.process_commands(message)


@bot.command()
@commands.is_owner()
async def sync(ctx: commands.Context):
    """Syncs slash commands to Discord
    Can only be run by the bot owner"""
    await bot.tree.sync()
    print(f"{ctx.author} Synced slash commands")


@bot.hybrid_command(
    name="ping",
    with_app_command=True,
    description="""Displays the latency in ms in a Discord Embed.
                        The colour of the embed shows whether this good or bad""",
)
@commands.bot_has_permissions(view_channel=True, send_messages=True)
async def ping(ctx: commands.Context):
    """Displays the latency in ms in a Discord Embed.
    The colour of the embed shows whether this good or bad"""
    rounded_latency_time = round(bot.latency * 1000)
    if rounded_latency_time <= 50:
        embed = discord.Embed(
            title="PONG",
            description=f":ping_pong: The ping is **{rounded_latency_time}** milliseconds!",
            color=0x44FF44,
        )
    elif rounded_latency_time <= 100:
        embed = discord.Embed(
            title="PONG",
            description=f":ping_pong: The ping is **{rounded_latency_time}** milliseconds!",
            color=0xFFD000,
        )
    elif rounded_latency_time <= 200:
        embed = discord.Embed(
            title="PONG",
            description=f":ping_pong: The ping is **{rounded_latency_time}** milliseconds!",
            color=0xFF6600,
        )
    else:
        embed = discord.Embed(
            title="PONG",
            description=f":ping_pong: The ping is **{rounded_latency_time}** milliseconds!",
            color=0x990000,
        )
    await ctx.send(embed=embed)


bot.run(TOKEN)
