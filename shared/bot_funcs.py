from bot import bot
from classesStructure.classStructures import botMessage
from keyboards.inline_keyboards.pickup_kb import build_first_kb


async def callBot(obj, chatId):
    await bot.send_message(chat_id=chatId, text=obj, reply_markup=build_first_kb(botMessage.deliveryBtns))

