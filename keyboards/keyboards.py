from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

m = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="jam"),
         KeyboardButton(text="links")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Choose",
    selective=True
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="link1", callback_data="linkone"),
            InlineKeyboardButton(text="link1", callback_data="linktwo")
        ]
    ]
)

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Принять", callback_data="accept"),
        ]
    ]
)

second = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Далее", callback_data="next"),
            InlineKeyboardButton(text="Отложить", callback_data="delay"),
            InlineKeyboardButton(text="Отменить", callback_data="cancel"),
        ]
    ],

)

third = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Далее", callback_data="next"),
            InlineKeyboardButton(text="Отменить", callback_data="cancel"),
            InlineKeyboardButton(text="Ложный вызов", callback_data="fake_button"),
            InlineKeyboardButton(text="Починил на мест", callback_data="fix_button"),
        ]
    ]
)

fourth = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Далее", callback_data="next"),
            InlineKeyboardButton(text="Отменить", callback_data="cancel"),
            InlineKeyboardButton(text="Ложный вызов", callback_data="fake_button"),
            InlineKeyboardButton(text="Починил на мест", callback_data="fix_button"),
        ]
    ]
)


