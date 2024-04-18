from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

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


@router.message(RegisterMessage.comment_response, F.data.in_({'comment'}))
async def process_comment(msg: Message, state: FSMContext):
    print('call.message.text', msg.text)
    await state.update_data(comment_msg=msg.text)
    await msg.answer('Comment section')
    await save_comment_action(botMessage.user_token, {
        'object': botMessage.objectMessage['id'],
        'comment': msg.text
    })
    print('data', botMessage.deliveryBtns)


@router.callback_query(
    PickupCbData.filter(F.action.in_({'1', '2',
                                      '3',
                                      '4',
                                      '6'}))
)
async def process_second_kb(call: CallbackQuery, callback_data: PickupCbData):
    print('call.data', call.data)
    print('hjvjb', botMessage.objectMessage)
    print('PickupCbData', callback_data.call_back)

    await save_btn_action(botMessage.user_token, {
        'order': botMessage.objectMessage['id'],
        'button': callback_data.call_back
    })
    print('data', botMessage.deliveryBtns)
    await call.answer()
    await call.message.edit_reply_markup(
        text="Your shop actions:",
        reply_markup=build_first_kb(botMessage.deliveryBtns)
    )


@router.callback_query(
    PickupCbData.filter(F.action.in_({
        '5',
        '7',
        '8',
        '9',
        '10', '11'}))
)
async def process_comment_kb(call: CallbackQuery, callback_data: PickupCbData):
    print('call.message.text', call.message.text)
    await call.answer('Enter your comment to order')
    await save_comment_action(botMessage.user_token, {
        'object': botMessage.objectMessage['id'],
        'comment': call.message.text
    })
    print('data', botMessage.deliveryBtns)
