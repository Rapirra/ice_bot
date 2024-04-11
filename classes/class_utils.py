from aiogram.filters.callback_data import CallbackData


class HandlerCallbackClass(CallbackData, prefix="iceberg"):
    text: str
    callback_data: str