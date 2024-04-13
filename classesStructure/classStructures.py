from aiogram.fsm.state import StatesGroup, State


class RegisterMessages(StatesGroup):
    userToken = State()


class SubscriptionStates(StatesGroup):
    sendingResponse = State()
