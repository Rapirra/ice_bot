from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class PickupCbData(CallbackData, prefix="pickup"):
    action: str
    btn_text: str
    call_back: str


dictObj = {
    1: {'name': 'start', 'event': 0, 'color': '#3096CF', 'id': '1', 'key': '1'},
    2: {'name': 'decline', 'event': 2, 'color': '#808080', 'id': '2', 'key': '2'},
    3: {'name': 'defer', 'event': 3, 'color': '#F1B500', 'id': '3', 'key': '3'},
    4: {'name': 'go-next', 'event': 0, 'color': '#00A329', 'id': '4', 'key': '4'},
    5: {'name': 'fix', 'event': 10, 'color': '#808080', 'id': '5', 'key': '5'},
    6: {'name': 'false-alarm', 'event': 10, 'color': '#808080', 'id': '6', 'key': '6'},
    7: {'name': 'defer-decline', 'event': 3, 'color': '#EB9947', 'id': '7', 'key': '7'},
    8: {'name': 'client-cancel', 'event': 9, 'color': '#CC3333', 'id': '8', 'key': '8'},
    9: {'name': 'complete-delivery', 'event': 11, 'color': '#3096CF', 'id': '9', 'key': '9'},
    10: {'name': 'complete-pickup', 'event': 8, 'color': '#3096CF', 'id': '10', 'key': '10'},
    11: {'name': 'complete-pickup', 'event': 8, 'color': '#3096CF', 'id': '11', 'key': '11'}
}


def build_first_kb(obj) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in obj:
        print('item', item)
        btn_text = dictObj[item['key']]['name']
        event_value = dictObj[item['key']]
        call_back = event_value['id'] if event_value['id'] is not None else '1'
        print(btn_text, call_back)
        builder.add(InlineKeyboardButton(
            text=btn_text,
            callback_data=PickupCbData(action=call_back, btn_text=btn_text, call_back=call_back).pack()
        ))
        builder.adjust(2)
    return builder.as_markup()



