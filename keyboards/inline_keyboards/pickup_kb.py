from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class PickupCbData(CallbackData, prefix="pickup"):
    action: str
    btn_text: str
    call_back: str
    order_id: int


dictObj = {
    1: {'name': 'start', 'event': 0, 'color': '#3096CF', 'id': '1', 'key': '1'},
    2: {'name': 'go-next', 'event': 0, 'color': '#00A329', 'id': '2', 'key': '2'},
    3: {'name': 'defer', 'event': 3, 'color': '#F1B500', 'id': '3', 'key': '3'},
    4: {'name': 'decline', 'event': 2, 'color': '#CC3333', 'id': '4', 'key': '4'},
    5: {'name': 'fix', 'event': 10, 'color': '#808080', 'id': '5', 'key': '5'},
    6: {'name': 'false-alarm', 'event': 10, 'color': '#808080', 'id': '6', 'key': '6'},
    7: {'name': 'defer-decline', 'event': 3, 'color': '#EB9947', 'id': '7', 'key': '7'},
    8: {'name': 'client-cancel', 'event': 9, 'color': '#CC3333', 'id': '8', 'key': '8'},
    9: {'name': 'complete-delivery', 'event': 11, 'color': '#3096CF', 'id': '9', 'key': '9'},
    10: {'name': 'complete-pickup', 'event': 8, 'color': '#3096CF', 'id': '10', 'key': '10'},
    11: {'name': 'payment', 'event': 8, 'color': '#3096CF', 'id': '11', 'key': '11'}
}


def build_first_kb(obj, order_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    str_order = str(order_id)
    for item in obj:
        btn_text = dictObj[item['id']]['name']
        event_value = str(item['key'])
        builder.add(InlineKeyboardButton(
            text=btn_text,
            callback_data=PickupCbData(action=event_value, btn_text=btn_text, call_back=event_value, order_id=str_order).pack()
        ))
        builder.adjust(2)
    return builder.as_markup()



