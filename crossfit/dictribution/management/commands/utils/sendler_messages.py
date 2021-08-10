from content.management.commands.loader import dp
from .make_message import DictributionMessage
import time
from content.models import TelegramUser
import logging


async def send_dictribution(dictribution):
    logging.info(f'start dictribution: {dictribution.name}')
    message = DictributionMessage(dictribution).get_as_python()
    for user in TelegramUser.objects.all():
        try:
            await dp.bot.send_message(chat_id=user.telegram_id, **message)
            time.sleep(0.5)
        except:
            pass
    logging.info(f'end dictribution: {dictribution.name}')
