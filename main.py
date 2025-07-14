import asyncio
import logging
import sys

from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN
from handlers import start

dp = Dispatcher()


async def set_command(bot: Bot):
    commands = [
        BotCommand(command="start", description="Старт"),
    ]
    await bot.set_my_commands(commands)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await set_command(bot)
    dp.include_router(start.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

