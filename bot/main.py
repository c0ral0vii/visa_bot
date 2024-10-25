from aiogram import Dispatcher, Bot, types
from handlers.start_handler import start_router
from config.config import config


bot = Bot(token=config.BOT_API)
dp = Dispatcher()

dp.include_routers()

async def on_startup(dp):
    commands = [
        types.BotCommand(command='/start', description='Запуск бота'),
    ]
    await bot.set_my_commands(commands)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    await on_startup(dp)
    await dp.start_polling()