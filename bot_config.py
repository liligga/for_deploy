from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from database.database import Database


load_dotenv()
database = Database("db.sqlite3")
dev = getenv("DEV", 0)
if not dev:
    from aiogram.client.session.aiohttp import AiohttpSession

    print("started on serve")
    session = AiohttpSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("BOT_TOKEN"), session=session)

else:
    print("started on dev")
    bot = Bot(token=getenv("BOT_TOKEN"))

dp = Dispatcher()