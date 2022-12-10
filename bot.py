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
                name="Watching you",
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

    # if message.content.startswith("smcm sc"):
    #     score_unavailable_message = (
    #         "`smcm score` has now been replaced with: `mcm score` or `/score`"
    #     )
    #     await message.channel.send(score_unavailable_message)
    #
    # if message.author.id == OWO_BOT_ID:
    #     if "sacrificed" in message.content:
    #         await message.reply(gif_links.get_sacrifice())
    #     elif "sold" in message.content:
    #         await message.reply(gif_links.get_money())
    #     elif "you currently have **__0__ cowoncy!**" in message.content:
    #         await message.reply(gif_links.get_no_money())
    #     elif (
    #         "finished a quest and earned:" in message.content
    #         or "leveled up!" in message.content
    #     ):
    #         await message.reply(gif_links.get_applause())

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


# @bot.hybrid_command(
#     name="score", with_app_command=True, description="Displays the player's score"
# )
# @commands.bot_has_permissions(view_channel=True, send_messages=True)
# async def score(ctx: commands.Context):
#     """Displays the player's score"""
#
#     embed = discord.Embed(
#         title=f"{ctx.author.display_name}'s Score \n(**NOT WORKING YET!! COMING SOON**)",
#         description=":medal::medal::medal::medal:",
#         color=0x44FF44,
#     )
#     embed.add_field(
#         name="OwO Scores:",
#         value="`owo`: 0 \n" "`hunt`: 0 \n" "`battle`: 0 \n\n" "**Your Score: 0**",
#         inline=True,
#     )
#     await ctx.send(embed=embed)


bot.run(TOKEN)
