from loguru import logger as log
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


bot = Bot(token='7036317929:AAG5Ha-y3xavzO_wl-Es0G4Hyp7Mr19G3v0')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет обжора!')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нужна помощь? Неужто отравился?')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info('Бот остановлен.')
