from typing import TYPE_CHECKING

from discord import Emoji, Message, TextChannel
from discord.ext import commands
from discord.ext.commands import Context, command

if TYPE_CHECKING:
    Bot = commands.Bot[Context]
    Cog = commands.Cog[Context]
else:
    Bot = commands.Bot
    Cog = commands.Cog


class Main(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @property
    def nut_emoji(self) -> Emoji:
        nut_emoji = self.bot.get_emoji(780844352129073182)
        assert nut_emoji is not None, "Nut emohi is not available here"
        return nut_emoji

    @command()
    async def nut(self, ctx: Context) -> None:
        await ctx.send(self.nut_emoji)

    @command()
    async def repeat(self, ctx: Context, message: str) -> None:
        await ctx.send(f"You said: {message}")

    @command()
    async def hello(self, ctx: Context, message: str) -> None:
        await ctx.send(f"You said: {message}")

    @Cog.listener()
    async def on_ready(self) -> None:
        print(f"We have logged in as {self.bot.user}")

    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        channel = message.channel
        if isinstance(channel, TextChannel) and channel.name != "bot-tests":
            return

        a = message.author
        print(type(a))
        print(f"Name: {a.name}")
        print(f"ID: {a.id}")
        if message.author == self.bot.user:
            return

        if message.content == "test":
            await message.channel.send(f"Testing this for you <@{a.id}>", tts=True)

        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")
