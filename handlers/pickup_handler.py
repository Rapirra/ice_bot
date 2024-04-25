from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from gql.transport.exceptions import TransportQueryError

from classesStructure.classStructures import RegisterMessage, create_tg_class
from keyboards.inline_keyboards.pickup_kb import PickupCbData, build_first_kb
from models.resolvers.auth_resolver import initialize_graphql, establish_http_connection
from models.resolvers.btns_resolver import save_btn_action, save_comment_action
from shared.bot_funcs import delete_msgs

router = Router(name=__name__)

global bot_msg_class


async def create_class(chat_id):
    global bot_msg_class
    bot_msg_class = await create_tg_class(chat_id)
    return bot_msg_class


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer('Welcome. Please enter your token', parse_mode="HTML")
    await state.set_state(RegisterMessage.user_token)
    await create_class(message.chat.id)


@router.message(RegisterMessage.user_token)
async def extract_data(message: Message, state: FSMContext):
    await state.update_data(user_token=message.text)
    # message.from_user.id
    bot_msg_class.adduser_token(message.text)
    try:
        result = await establish_http_connection(message.text, bot_msg_class)
        await message.answer(result)
        if not isinstance(result, TransportQueryError):
            await state.set_state(RegisterMessage.user_socket_me)
            await initialize_graphql(bot_msg_class.user_token, message.chat.id, bot_msg_class)
        else:
            raise TransportQueryError
    except Exception as e:
        await message.answer(f"Enter valid token")
        await state.set_state(RegisterMessage.user_token)


@router.message(RegisterMessage.user_socket_me)
async def extract_data_socket(message: Message, state: FSMContext):
    await initialize_graphql(bot_msg_class.user_token, message.chat.id)
    await state.set_state(RegisterMessage.comment_request)


@router.callback_query(PickupCbData.filter(F.action.in_({'1', '2', '3', '4', '6'})))
async def process_second_kb(call: CallbackQuery, callback_data: PickupCbData):
    await save_btn_action(bot_msg_class.user_token, {
        'order': int(callback_data.order_id),
        'button': callback_data.call_back
    }, bot_msg_class)
    await call.answer()
    await call.message.edit_reply_markup(
        text="Your shop actions:",
        reply_markup=build_first_kb(bot_msg_class.deliveryBtns.get(callback_data.order_id), callback_data.order_id)
    )


@router.callback_query(PickupCbData.filter(F.action.in_({'5', '7', '8', '9', '10', '11'})) or
                       RegisterMessage.comment_request)
async def process_comment_kb(call: CallbackQuery, callback_data: PickupCbData, state: FSMContext):
    await state.update_data(comment_request_msg_id=call.message.message_id)
    bot_msg_class.add_order_related_message(call.message.message_id, callback_data.order_id)
    await state.set_state(RegisterMessage.order_register_id)
    await state.update_data(order_register_id=callback_data.order_id)
    bot_msg_class.add_order_related_message(call.message.message_id, callback_data.order_id)
    await state.set_state(RegisterMessage.comment_handle)
    await save_btn_action(bot_msg_class.user_token, {
        'order': int(callback_data.order_id),
        'button': callback_data.call_back
    }, bot_msg_class)
    sent_message = await call.message.answer('Enter your comment to order')
    bot_msg_class.add_order_related_message(sent_message.message_id, callback_data.order_id)
    await state.update_data(comment_handle_msg_id=sent_message.message_id)
    await state.set_state(RegisterMessage.comment_text)


@router.message(RegisterMessage.comment_text)
async def process_comment_kb(message: Message, state: FSMContext):
    msg_id = await state.get_data()
    if message.text:
        await save_comment_action(bot_msg_class.user_token, {
            'object': msg_id['order_register_id'],
            'comment': message.text
        })
        bot_msg_class.add_order_related_message(message.message_id, msg_id['order_register_id'])
        print(bot_msg_class.order_related_messages)
        order_msgs = bot_msg_class.order_related_messages.get(msg_id['order_register_id'])
        await delete_msgs(order_msgs, message.chat.id)
        await state.clear()
