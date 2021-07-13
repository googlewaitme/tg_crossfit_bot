from content.models import ButtonOneText


def get_message_one_button(button_name):
    '''
    В боте очень много кнопок, который отправляют текст
    с какой-то нагрузкой и актуальностью. Поэтому нужно
    иметь возможность обновлять их, без изменения в коде.
    '''
    defaults = {'description': 'Создана новый кнопка!!!',
                'text': f'Текста для {button_name} нет, просьба заполнить!'}
    button, created = ButtonOneText.objects.get_or_create(
        name=button_name, defaults=defaults)
    return button.text
