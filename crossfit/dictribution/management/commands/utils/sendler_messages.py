from content.management.commands.loader import dp
from .make_message import DictributionMessage
import time
from contextlib import suppress
from content.models import TelegramUser
from aiogram.utils.exceptions import ChatNotFound
import logging


async def send_dictribution(dictribution):
    logging.info(f'start dictribution: {dictribution.name}')
    message = DictributionMessage(dictribution).get_as_python()
    for user in TelegramUser.objects.all():
        with suppress(ChatNotFound):
            await dp.bot.send_message(chat_id=user.telegram_id, **message)
            time.sleep(0.5)
    logging.info(f'end dictribution: {dictribution.name}')
