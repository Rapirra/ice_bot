import logging
from aiogram import Bot, Dispatcher
from config.config import load_config, Config


config: Config = load_config()
bot = Bot(token=config.tg_bot)
url_graphql = config.url
dispatcher = Dispatcher()
logging.basicConfig(level=logging.INFO)