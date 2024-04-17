from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class PickupCbData(CallbackData, prefix="pickup"):
    action: str


dictObj = {
    1: {'name': 'start', 'event': 0, 'color': '#3096CF', 'id': '1'},
    2: {'name': 'go-next', 'event': 0, 'color': '#00A329', 'id': '2'},
    3: {'name': 'defer', 'event': 3, 'color': '#F1B500', 'id': '3'},
    4: {'name': 'decline', 'event': 2, 'color': '#808080', 'id': '4'},
    5: {'name': 'fix', 'event': 10, 'color': '#808080', 'id': '5'},
    6: {'name': 'false-alarm', 'event': 10, 'color': '#808080', 'id': '6'},
    7: {'name': 'defer-decline', 'event': 3, 'color': '#EB9947', 'id': '7'},
    8: {'name': 'client-cancel', 'event': 9, 'color': '#CC3333', 'id': '8'},
    9: {'name': 'complete-delivery', 'event': 11, 'color': '#3096CF', 'id': '9'},
    10: {'name': 'complete-pickup', 'event': 8, 'color': '#3096CF', 'id': '10'}
}


def build_first_kb(obj) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in obj:
        btn_text = dictObj[item['type']]['name']
        button_dict = item['button']
        event_value = button_dict.get('id', None) if isinstance(button_dict, dict) else None

        call_back = event_value if event_value is not None else 'accept'
        builder.add(InlineKeyboardButton(
            text=btn_text,
            callback_data=PickupCbData(action=call_back).pack()
        ))

    return builder.as_markup()
