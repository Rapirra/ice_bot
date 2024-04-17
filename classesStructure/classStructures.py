from aiogram.fsm.state import StatesGroup, State

class BotMessage:
    user_token = ''
    objectMessage = {}

    logic = False
    deliveryBtns = None

    def adduser_token(self, user_token):
        self.user_token = user_token

    def addObjMessage(self, objectMessage):
        self.objectMessage = objectMessage
        self.logic = True


class RegisterMessage(StatesGroup):
    user_token = State()
    chat_id = State()


class SubscriptionStates(StatesGroup):
    sendingResponse = State()


botMessage = BotMessage()




