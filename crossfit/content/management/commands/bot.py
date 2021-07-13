from django.core.management.base import BaseCommand
from django.conf import settings
from aiogram import executor
from .loader import dp
from . import handlers
from .utils.notify_admins import on_startup_notify
from .utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **kwargs):
        executor.start_polling(dp, on_startup=on_startup)
