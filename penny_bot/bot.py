from typing import TYPE_CHECKING

from discord.ext import commands
from discord.ext.commands import Context

from penny_bot.main import Main

if TYPE_CHECKING:
    Bot = commands.Bot[Context]
else:
    Bot = commands.Bot


def create_bot() -> Bot:
    bot = Bot(command_prefix="?")
    bot.add_cog(Main(bot))
    return bot
