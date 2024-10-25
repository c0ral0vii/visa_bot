from aiogram import Bot


async def notify_user(bot: Bot, user_id: int, message: str):
    '''
    Отправка уведомления пользователю
    '''

    await bot.send_message(user_id, message)