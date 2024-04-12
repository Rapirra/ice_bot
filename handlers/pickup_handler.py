from aiogram import Router, F, html
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from keyboards.inline_keyboards.pickup_kb import build_first_kb, PickupCbData, CourierActions, build_second_kb, \
    build_third_kb, build_fourth_kb
from bot import bot

router = Router(name=__name__)


class RegisterMessages(StatesGroup):
    userEmail = State()
    userPassword = State()


class DB:
    answer_data = {}


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer('Enter your token', parse_mode="HTML")


@router.message(F.text)
async def extract_data(message: Message):
    await message.answer(f"Your token {message.text}\n\n", parse_mode="HTML")


@router.callback_query(
    PickupCbData.filter(F.action == CourierActions.accept)
)
async def process_second_kb(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        text="Your shop actions:",
        reply_markup=build_first_kb(),
    )


@router.callback_query(
    PickupCbData.filter(F.action == CourierActions.second)
)
async def process_second_kb(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        text="Your shop actions:",
        reply_markup=build_second_kb(),
    )


@router.callback_query(
    PickupCbData.filter(F.action == CourierActions.third)
)
async def process_third_kb(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        text="Your shop actions:",
        reply_markup=build_third_kb(),
    )


@router.callback_query(
    PickupCbData.filter(F.action == CourierActions.fourth)
)
async def process_fourth_kb(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        text="Your shop actions:",
        reply_markup=build_fourth_kb(),
    )
