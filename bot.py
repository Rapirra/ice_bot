import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, BaseMiddleware, Router, html
from aiogram.methods import SendMessage
import os
from dotenv import load_dotenv
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()

bot = Bot(token=os.getenv('API_TOKEN'))

dp = Dispatcher()
router1 = Router()
dp.include_router(router1)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello,knjkn!")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
