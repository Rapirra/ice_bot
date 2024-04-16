from enum import IntEnum, auto, Enum, Flag

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class CourierActions(Enum):
    accept = 'accept'
    second = 'second'
    third = 'third'
    fourth = 'fourth'
    delay = 'delay'
    cancel = 'cancel'
    fake = 'fake'
    fix = 'fix'
    complete = 'complete'


class PickupCbData(CallbackData, prefix="pickup"):
    action: CourierActions


dictObj = {
    1: {'name': 'start', 'event': 0, 'color': '#3096CF'},
    2: {'name': 'go-next', 'event': 0, 'color': '#00A329'},
    3: {'name': 'defer', 'event': 3, 'color': '#F1B500'},
    4: {'name': 'decline', 'event': 2, 'color': '#808080'},
    5: {'name': 'fix', 'event': 10, 'color': '#808080'},
    6: {'name': 'false-alarm', 'event': 10, 'color': '#808080'},
    7: {'name': 'defer-decline', 'event': 3, 'color': '#EB9947'},
    8: {'name': 'client-cancel', 'event': 9, 'color': '#CC3333'},
    9: {'name': 'complete-delivery', 'event': 11, 'color': '#3096CF'},
    10: {'name': 'complete-pickup', 'event': 8, 'color': '#3096CF'}
}

thirdBtn = InlineKeyboardButton(text='Next',
                                callback_data=PickupCbData(action=CourierActions.third).pack())
fourthBtn = InlineKeyboardButton(text='Next',
                                 callback_data=PickupCbData(action=CourierActions.fourth).pack())
acceptBtn = InlineKeyboardButton(text='Accept',
                                 callback_data=PickupCbData(action=CourierActions.accept).pack())
delayBtn = InlineKeyboardButton(text='Delay',
                                callback_data=PickupCbData(action=CourierActions.delay).pack())
cancelBtn = InlineKeyboardButton(text='Cancel',
                                 callback_data=PickupCbData(action=CourierActions.cancel).pack())
fakeBtn = InlineKeyboardButton(text='Fake',
                               callback_data=PickupCbData(action=CourierActions.fake).pack())
fixBtn = InlineKeyboardButton(text='Fix',
                              callback_data=PickupCbData(action=CourierActions.fix).pack())
completeBtn = InlineKeyboardButton(text='Complete',
                                   callback_data=PickupCbData(action=CourierActions.complete).pack())


def build_first_kb(obj) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in obj:
        btn_text = dictObj[item['type']]['name']
        button_dict = item['button']
        event_value = button_dict.get('event', None) if isinstance(button_dict, dict) else None

        call_back = event_value if event_value is not None else 'accept'
        builder.add(InlineKeyboardButton(
            text=btn_text,
            callback_data=PickupCbData(action=CourierActions(call_back)).pack()
        ))

    return builder.as_markup()


def build_second_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(thirdBtn, delayBtn, cancelBtn)
    return builder.as_markup()


def build_third_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(fourthBtn, cancelBtn, fakeBtn, fixBtn)
    return builder.as_markup()


def build_fourth_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(completeBtn, cancelBtn)
    return builder.as_markup()
