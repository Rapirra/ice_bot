from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from classesStructure.classStructures import botMessage, RegisterMessage
from models.auth import client, initializeGraphql, callBot

router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer('Enter your token', parse_mode="HTML")
    await state.set_state(RegisterMessage.user_token)


@router.message(RegisterMessage.user_token, F.text)
async def extract_data(message: Message, state: FSMContext):
    await state.update_data(userToken=message.text)
    user_data = await state.get_data()
    if user_data:
        botMessage.addUserToken(message.text)
    await message.answer(
        text=f"Your token {user_data['userToken']}."
    )
    if botMessage.userToken:
        await initializeGraphql(botMessage.userToken, message.chat.id)





# @router.message_reaction()
# async def process_second_kb(call: CallbackQuery):
#
#     await call.answer()
#     await call.message.answer(
#         text="Your shop actions:",
#         reply_markup=build_first_kb(),
#     )
#
#
# @router.callback_query(
#     PickupCbData.filter(F.action == CourierActions.second)
# )
# async def process_second_kb(call: CallbackQuery):
#     await call.answer()
#     await call.message.answer(
#         text="Your shop actions:",
#         reply_markup=build_second_kb(),
#     )
#
#
# @router.callback_query(
#     PickupCbData.filter(F.action == CourierActions.third)
# )
# async def process_third_kb(call: CallbackQuery):
#     await call.answer()
#     await call.message.answer(
#         text="Your shop actions:",
#         reply_markup=build_third_kb(),
#     )
#
#
# @router.callback_query(
#     PickupCbData.filter(F.action == CourierActions.fourth)
# )
# async def process_fourth_kb(call: CallbackQuery):
#     await call.answer()
#     await call.message.answer(
#         text="Your shop actions:",
#         reply_markup=build_fourth_kb(),
#     )
