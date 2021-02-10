import os

from penny_bot.bot import create_bot

TOKEN = os.environ["DISCORD_BOT_TOKEN"]


if __name__ == "__main__":
    bot = create_bot()
    bot.run(TOKEN)
