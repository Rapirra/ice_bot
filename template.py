
order_template = 'Заказ №A40 ( На заборе )\n' + 'Забрать в 2024.05.12 12:30\n' + 'Клиент: Альгафур(+7(700)-268-43-07)\n' + 'Адрес: Абая 62'

accept_button = {
        'title':  'Принять',
        'key': '1'
    }

next_button = {
        'title':  'Далее',
        'key': '2'
    }

delay_button = {
        'title':  'Отложить',
        'key': '3'
    }

cancel_button = {
        'title':  'Отменить',
        'key': '4'
    }

complete_button = {
        'title':  'Завершить',
        'key': '5'
    }

fake_button = {
        'title':  'Ложный вызов',
        'key': '6'
    }

fix_button = {
        'title':  'Починил на месте',
        'key': '7'
    }



pickup_actions = {
    'first': ( accept_button ), # step first courier receive order
    'second': ( next_button, delay_button, cancel_button ), # call to client
    'third': ( next_button, cancel_button, fake_button, fix_button ), # delivered to client
    'fourth': ( complete_button, cancel_button ) #
}

delivery_actions = {
    'first': ( accept_button ), # step first courier receive order
    'second': ( next_button, delay_button, cancel_button ), # call to client
    'third': ( next_button, delay_button, cancel_button ), # delivered to client
    'fourth': ( complete_button, cancel_button ) #
}