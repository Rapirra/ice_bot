from aiogram.fsm.state import StatesGroup, State


class RegisterMessage(StatesGroup):
    user_token = State()
    user_socket_me = State()
    chat_id = State()
    comment_request = State()
    comment_text = State()
    comment_handle = State()
    order_register_id = State()