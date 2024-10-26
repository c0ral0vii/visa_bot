from aiogram import Dispatcher, Bot, types
from bot.handlers.start_handler import start_router
from config.config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.include_router(start_router)


async def on_startup(dp):
    commands = [
        types.BotCommand(command='/start', description='Запуск бота'),
    ]
    await bot.set_my_commands(commands)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    await on_startup(dp=dp)
    await dp.start_polling(bot)
