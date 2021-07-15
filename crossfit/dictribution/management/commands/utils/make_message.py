from dictribution.models import Dictribution
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class DictributionMessage:
    def __init__(self, dictribution: Dictribution):
        self.message = types.Message()
        self.dictribution = dictribution

    def get_as_python(self):
        self.make()
        return self.message.to_python()

    def make(self):
        self.add_text()
        self.add_inline_button()
        self.add_content()

    def add_text(self):
        self.message.text = self.dictribution.text

    def add_inline_button(self):
        if self.dictribution.button_url:
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton(
                    text=self.dictribution.button_name,
                    url=self.dictribution.button_url)
            )
            self.message.reply_markup = markup

    def add_content(self):
        if not self.dictribution.content_url:
            return
        url = f'<a href="{self.dictribution.content_url}"> </a>'
        self.message.text = url + self.message.text
