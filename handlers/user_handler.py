from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from classes.class_utils import HandlerCallbackClass
from keyboards.keyboards import second, third

router = Router()


def createKeyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Принять", callback_data=HandlerCallbackClass(text="accept", callback_data="accept"))
    return builder.as_markup()


cb = CallbackData('ikb', 'action')

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Далее", callback_data="next"),
            InlineKeyboardButton(text="Отложить", callback_data="delay"),
            InlineKeyboardButton(text="Отменить", callback_data="cancel"),
        ]
    ]
)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Hi banshee pickup_actions', reply_markup=createKeyboard())


@router.callback_query(HandlerCallbackClass.filter(F.callback_data == "accept"))
async def callback_func(callback: CallbackQuery, callback_data: HandlerCallbackClass):
    await callback.message.edit_text('jira', reply_markup=second)


@router.callback_query()
async def process_second_keyboard(callback: CallbackQuery):
    if callback.data == 'next':
        print(f'{callback.data}')
        await callback.message.answer('You clicked', reply_markup=third)


@router.callback_query(F.text.in_(['next', 'cancel', 'fake_button', 'fix_button']))
async def process_third_keyboard(callback: CallbackQuery):
    await callback.message.answer(f'You clicked: {callback.data}')


@router.callback_query(text="show_card")
async def process_show_card_button(callback: CallbackQuery):
    await callback.answer(show_alert=True,
                          text=str(callback.data))


@router.callback_query(text="complete_button")
async def process_complete_button(callback: CallbackQuery):
    await callback.message.delete()


@router.callback_query(cb.filter())
async def process_cd(callback: CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await callback.answer('Pushed')
