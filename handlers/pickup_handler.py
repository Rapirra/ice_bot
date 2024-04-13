from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline_keyboards.pickup_kb import build_first_kb, PickupCbData, CourierActions, build_second_kb, \
    build_third_kb, build_fourth_kb
from models.auth import client
from models.order import query

router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    print(message.chat.id)
    await message.answer('Enter your token', parse_mode="HTML")
    await state.set_state(RegisterMessages.userToken)


@router.message(RegisterMessages.userToken, F.text)
async def extract_data(message: Message, state: FSMContext):
    await state.update_data(userToken=message.text.lower())
    user_data = await state.get_data()
    print(user_data)
    await message.answer(
        text=f"Your token {user_data['userToken']}."
    )
    await state.set_state(SubscriptionStates.sendingResponse)


@router.message(RegisterMessages.userToken, F.text)
async def make_async_request(message: Message, state: FSMContext):
    data = await client.execute_async(query=query)
    await state.update_data(subscription_data=data)


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
