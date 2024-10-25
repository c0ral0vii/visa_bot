from aiogram import F, Router, types
from aiogram.filters import CommandStart

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start(message: types.Message):
    '''
    Команда start
    '''

    await message.answer('Тест')