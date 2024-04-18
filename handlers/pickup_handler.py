from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot import bot
from classesStructure.classStructures import botMessage, RegisterMessage
from keyboards.inline_keyboards.pickup_kb import PickupCbData, build_first_kb
from models.resolvers.auth_resolver import initialize_auth, initialize_graphql
from models.resolvers.btns_resolver import save_btn_action, save_comment_action

router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer('Enter your token', parse_mode="HTML")
    await state.set_state(RegisterMessage.user_token)


@router.message(RegisterMessage.user_token)
async def extract_data(message: Message, state: FSMContext):
    await state.update_data(user_token=message.text)
    botMessage.adduser_token(message.text)
    await state.set_state(RegisterMessage.chat_id)
    await state.update_data(chat=message.chat.id)
    if botMessage.user_token:
        result = await initialize_auth(message.text)
        await message.answer(text=result)
    await state.set_state(RegisterMessage.user_socket_me)


@router.message(RegisterMessage.user_socket_me)
async def connect_websocket(state: FSMContext, message: Message):
    await message.answer('hope')
    user_data = await state.get_data()
    print('user_data', user_data)
    await initialize_graphql(user_data['user_token'], message.chat.id)
    await state.set_state(RegisterMessage.comment_request)


@router.callback_query(PickupCbData.filter(F.action.in_({'1', '2', '3', '4', '6'})))
async def process_second_kb(call: CallbackQuery, callback_data: PickupCbData):
    await save_btn_action(botMessage.user_token, {
        'order': botMessage.objectMessage['id'],
        'button': callback_data.call_back
    })
    await call.answer()
    await call.message.edit_reply_markup(
        text="Your shop actions:",
        reply_markup=build_first_kb(botMessage.deliveryBtns)
    )


@router.callback_query(PickupCbData.filter(F.action.in_({'5', '7', '8', '10', '11'})),
                       RegisterMessage.comment_request)
async def process_comment_kb(call: CallbackQuery, callback_data: PickupCbData, state: FSMContext):
    await state.update_data(comment_request_msg_id=call.message.message_id)
    await state.set_state(RegisterMessage.comment_handle)
    await save_btn_action(botMessage.user_token, {
        'order': botMessage.objectMessage['id'],
        'button': callback_data.call_back
    })

    sent_message = await call.message.answer('Enter your comment to order')
    await state.update_data(comment_handle_msg_id=sent_message.message_id)
    await state.set_state(RegisterMessage.comment_text)


@router.message(RegisterMessage.comment_text)
async def process_comment_kb(message: Message, state: FSMContext):
    msg_id = await state.get_data()
    if message.text:
        await save_comment_action(botMessage.user_token, {
            'object': botMessage.objectMessage['id'],
            'comment': message.text
        })
        await bot.delete_message(chat_id=message.chat.id, message_id=msg_id['comment_request_msg_id'])
        await bot.delete_message(chat_id=message.chat.id, message_id=msg_id['comment_handle_msg_id'])
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await state.clear()

# @router.callback_query(PickupCbData.filter(F.action.in_({'9'})),
#                        RegisterMessage.comment_request)
# async def process_comment_kb(call: CallbackQuery, callback_data: PickupCbData, state: FSMContext):
#     await state.update_data(comment_request_msg_id=call.message.message_id)
#     await state.set_state(RegisterMessage.comment_handle)
#     await save_btn_action(botMessage.user_token, {
#         'order': botMessage.objectMessage['id'],
#         'button': callback_data.call_back
#     })
#
#     sent_message = await call.message.answer('Enter your comment to order')
#     await state.update_data(comment_handle_msg_id=sent_message.message_id)
#     await state.set_state(RegisterMessage.comment_text)
