
import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🎁 Добро пожаловать в Gift Guarant!\n\n"
        "Безопасный P2P-обмен Telegram Gifts и TON NFT.\n\n"
        "Команды: /help"
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "/start — запуск\n"
        "/deal — создать сделку\n"
        "/mydeals — мои сделки\n"
        "/rules — правила\n"
        "/support — поддержка"
    )


@dp.message(Command("deal"))
async def deal(message: Message):
    await message.answer("Создание сделок скоро будет доступно.")


@dp.message(Command("mydeals"))
async def mydeals(message: Message):
    await message.answer("У вас пока нет сделок.")


@dp.message(Command("rules"))
async def rules(message: Message):
    await message.answer("Правила сервиса в разработке.")


@dp.message(Command("support"))
async def support(message: Message):
    await message.answer("Поддержка скоро будет доступна.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
