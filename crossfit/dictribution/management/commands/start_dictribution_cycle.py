from django.core.management.base import BaseCommand
import time
from django.utils.timezone import now
from dictribution.models import Dictribution
from .utils.sendler_messages import send_dictribution
import asyncio


class Command(BaseCommand):
    help = 'Запуск цикла ожидания, новой рассылки'

    def handle(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        while True:
            query = Dictribution.objects.filter(is_sended=False, send_date_time__lte=now())
            dictributions = list(query)
            if dictributions:
                loop.run_until_complete(send_dictribution(dictributions[0]))
                dictributions[0].is_sended = True
                dictributions[0].save()
            time.sleep(300)
