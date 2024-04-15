from aiogram.fsm.state import StatesGroup, State


class BotMessage:
    userToken = None
    objectMessage = None

    def addUserToken(self, userToken):
        self.userToken = userToken

    def addObjMessage(self, objectMessage):
        self.objectMessage = objectMessage
        print(self.objectMessage)

    async def send_message_if_token_exists(self, bot):
        if self.userToken:
            await bot.send_message(self.userToken, self.objectMessage)
        else:
            print("User token is empty. Cannot send message.")


class RegisterMessage(StatesGroup):
    user_token = State()
    chat_id = State()


class SubscriptionStates(StatesGroup):
    sendingResponse = State()


botMessage = BotMessage()


async def processing_auto_message(chat_id, bot, bm):
    if bm.objectMessage:
        await bot.send_message(chat_id, f"hi banshee: {bm.objectMessage}")
    else:
        print("User token is empty. Cannot initialize GraphqlClient. Banshee i am here")
