import asyncio

from aiogram import Bot, Dispatcher
from environs import Env
from handlers import user_handler, file_handler

env = Env()
env.read_env()
token = env('TOKEN')

bot = Bot(token)
dp = Dispatcher()

async def main():

    dp.include_router(user_handler.router)
    dp.include_router(file_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())