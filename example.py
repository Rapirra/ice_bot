import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import dispatcher as dp, bot

router = Router()

builder = InlineKeyboardBuilder()
@router.message(CommandStart())
async def process_start_command(message: Message):
    builder.add(InlineKeyboardButton(text="link1", callback_data="linkone"),
            InlineKeyboardButton(text="link1", callback_data="linktwo"))
    jnjn = builder.as_markup()
    await message.answer('Enter your token', parse_mode="HTML", reply_markup=jnjn)


@router.callback_query(
    F.data.in_({'linkone', 'linktwo'})
)
async def process_fourth_kb(call: CallbackQuery):
    builder.add(InlineKeyboardButton(text="link1", callback_data="linkone"),
                InlineKeyboardButton(text="link1", callback_data="linktwo"))
    jnjn = builder.as_markup()
    await call.answer()
    await call.message.edit_reply_markup(
        text="Your shop actions:",
        reply_markup=jnjn,
    )


async def main():

    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())
