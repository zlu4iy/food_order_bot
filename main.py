from loguru import logger as log
from os import getenv
import logging

import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main


async def main():
    await async_main()
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=getenv('food_order_bot'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info('Бот остановлен.')
