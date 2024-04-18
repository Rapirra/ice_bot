from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot import bot
from classesStructure.classStructures import botMessage, RegisterMessage
from keyboards.inline_keyboards.pickup_kb import PickupCbData, build_first_kb
from models.resolvers.auth_resolver import initializeGraphql
from models.resolvers.btns_resolver import save_btn_action, save_comment_action

router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer('Enter your token', parse_mode="HTML")
    await state.set_state(RegisterMessage.user_token)


@router.message(RegisterMessage.user_token)
async def extract_data(message: Message, state: FSMContext):
    await state.update_data(user_token=message.text)
    user_data = await state.get_data()
    await state.set_state(RegisterMessage.comment_response)
    if user_data:
        botMessage.adduser_token(message.text)
    await message.answer('Successfully authorized, hi Banshee')
    if botMessage.user_token:
        await initializeGraphql(botMessage.user_token, message.chat.id)


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


@router.callback_query(PickupCbData.filter(F.action.in_({'5', '7', '8', '9', '10', '11'})),
                       RegisterMessage.comment_response)
async def process_comment_kb(call: CallbackQuery, callback_data: PickupCbData, state: FSMContext):
    await state.update_data(comment_msg_id=call.message.message_id)
    await save_btn_action(botMessage.user_token, {
        'order': botMessage.objectMessage['id'],
        'button': callback_data.call_back
    })
    await call.message.answer('Enter your comment to order')
    await state.set_state(RegisterMessage.comment_handle)


@router.message(RegisterMessage.comment_handle)
async def process_comment_kb(message: Message, state: FSMContext):
    msg_id = await state.get_data()
    if message.text:
        await save_comment_action(botMessage.user_token, {
            'object': botMessage.objectMessage['id'],
            'comment': message.text
        })
        await message.answer('Comment was sent Banshee')
        await bot.delete_message(chat_id=message.chat.id, message_id=msg_id['comment_msg_id'])
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
