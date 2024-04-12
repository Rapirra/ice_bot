from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from classes.class_utils import HandlerCallbackClass
from bot import bot
from keyboards.keyboards import first, second, third, fourth

router = Router()


def createKeyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Принять", callback_data=HandlerCallbackClass(text="accept", callback_data="accept"))
    return builder.as_markup()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Hi banshee pickup_actions', reply_markup=createKeyboard())


@router.callback_query(HandlerCallbackClass.filter(F.callback_data == "accept"))
async def callback_func(callback: CallbackQuery, callback_data: HandlerCallbackClass):
    await callback.message.edit_text('jira', reply_markup=second)


@router.callback_query()
async def process_second_keyboard(callback: CallbackQuery):
    if callback.data == 'next':
        print(f'{callback.data }')
        await callback.message.answer( 'You clicked', reply_markup=third)


@router.callback_query(F.text.in_(['next', 'cancel', 'fake_button', 'fix_button']))
async def process_third_keyboard(callback: CallbackQuery):
    await callback.message.answer(f'You clicked: {callback.data}')
