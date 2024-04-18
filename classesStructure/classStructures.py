from aiogram.fsm.state import StatesGroup, State


class BotMessage:
    user_token = ''
    objectMessage = {}
    deliveryBtns = None

    def adduser_token(self, user_token):
        self.user_token = user_token

    def addObjMessage(self, objectMessage):
        self.objectMessage = objectMessage

    def add_delivery_btns(self, delivery_btns):
        self.deliveryBtns = delivery_btns


class RegisterMessage(StatesGroup):
    user_token = State()
    chat_id = State()
    comment_request = State()
    comment_text = State()
    comment_handle = State()


botMessage = BotMessage()
