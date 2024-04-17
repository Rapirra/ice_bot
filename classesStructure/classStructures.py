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

    def get_obj(self):
        var = self.objectMessage


    async def send_message_if_token_exists(self, bot):
        if self.user_token:
            await bot.send_message(self.user_token, self.objectMessage)
        else:
            print("User token is empty. Cannot send message.")


class RegisterMessage(StatesGroup):
    user_token = State()
    chat_id = State()


class SubscriptionStates(StatesGroup):
    sendingResponse = State()


botMessage = BotMessage()




