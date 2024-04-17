from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from classesStructure.classStructures import botMessage, RegisterMessage
from keyboards.inline_keyboards.pickup_kb import PickupCbData, CourierActions, build_second_kb, \
    build_third_kb, build_fourth_kb, build_first_kb
from models.resolvers.auth_resolver import initializeGraphql
from models.resolvers.btns_resolver import save_btn_action

router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer('Enter your token', parse_mode="HTML")
    await state.set_state(RegisterMessage.user_token)


@router.message(RegisterMessage.user_token, F.text)
async def extract_data(message: Message, state: FSMContext):
    await state.update_data(user_token=message.text)
    user_data = await state.get_data()
    if user_data:
        botMessage.adduser_token(message.text)
    await message.answer('Successfully authorized, hi Banshee')
    if botMessage.user_token:
        await initializeGraphql(botMessage.user_token, message.chat.id)


@router.callback_query(
    PickupCbData.filter(F.action == CourierActions.accept)
)
async def process_second_kb(call: CallbackQuery):
    print('call.message', call.message)
    # user_token = get_user_token(call.from_user.id)
    # btn_event = get_btn_event(call.data)

    data = await save_btn_action(botMessage.user_token, {
        'button': 1,
        'order': 1
    })

    await call.answer()
    await call.message.answer(
        text="Your shop actions:",
        reply_markup=build_first_kb(data['deliveryButton'])
    )


@router.callback_query(
    PickupCbData.filter(F.action_in['2'])
)
async def process_third_kb(call: CallbackQuery):
    data = await save_btn_action(botMessage.user_token, {
        'button': 1,
        'order': 1
    })
    await call.answer()
    await call.message.answer(
        text="Your shop actions:",
        reply_markup=build_third_kb(),
    )


@router.callback_query(
    PickupCbData.filter(F.action == CourierActions.third)
)
async def process_fourth_kb(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        text="Your shop actions:",
        reply_markup=build_fourth_kb(),
    )
