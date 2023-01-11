"""Bot"""
import logging

import discord
from discord.ext import commands

import settings
from references import gif_links

logger = logging.getLogger("bot")
config = settings.Config().load()


class Bot(commands.Bot):
    """Prepares bot for use"""

    def __init__(self):
        intents: discord.Intents = discord.Intents(
            guilds=True,
            members=True,
            emojis=True,
            webhooks=True,
            presences=True,
            messages=True,
            reactions=True,
            message_content=True,
        )
        super().__init__(
            command_prefix=commands.when_mentioned_or("mcm ", "mcm"),
            case_insensitive=True,
            intents=intents,
            status=config.Status,
            activity=discord.Activity(
                type=int(config.ACTIVITY_TYPE),
                name=config.ACTIVITY_NAME,
            ),
        )

    async def on_command_error(self, ctx, error):  # pylint: disable=W0221
        await ctx.reply(error, ephemeral=True)


bot = Bot()


@bot.event
async def on_ready():
    """Logging out bot information at startup"""
    logger.info("%s", discord.version_info)
    logger.info("%s is connected to the following guilds:", bot.user)
    for guild in bot.guilds:
        logger.info("* %s (id: %s)", guild.name, guild.id)


@bot.event
async def on_message(message):
    """Actions based on messages read"""
    message.content = message.content.lower()
    if message.author == bot.user:
        return

    if message.content == "hi":
        await message.channel.send(gif_links.get_hello())

    await bot.process_commands(message)


@bot.command(hidden=True)
@commands.is_owner()
async def sync(ctx: commands.Context):
    """Syncs slash commands to Discord
    Can only be run by the bot owner"""
    await bot.tree.sync()
    await ctx.send(f"{ctx.author.display_name} Synced slash commands")


@bot.hybrid_command(
    name="ping",
    with_app_command=True,
    help="""Displays the latency in ms.
    The colour of the embed shows whether this is;
    good (green),
    acceptable (orange),
    or bad (red)""",
)
@commands.bot_has_permissions(view_channel=True, send_messages=True)
async def ping(ctx: commands.Context):
    """Displays the latency in ms"""
    rounded_latency_time = round(bot.latency * 1000)
    if rounded_latency_time <= 50:
        colour = 0x44FF44
    elif rounded_latency_time <= 150:
        colour = 0xFF6600
    else:
        colour = 0x990000
    embed = discord.Embed(
        title="PONG",
        description=f":ping_pong: The ping is **{rounded_latency_time}** milliseconds!",
        color=colour,
    )

    await ctx.send(embed=embed)


bot.run(config.BOT_TOKEN, root_logger=True)
