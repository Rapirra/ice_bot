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


def build_first_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(acceptBtn)
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
