from lib.ChatCache import ChatCache


class TelegramBotCache:
    __instance = None
    chat_messages = {}

    def __new__(cls, chat_id):
        print('cls.chat_messages',cls.chat_messages)
        if not hasattr(cls, '__instance'):
            cls.__instance = super(TelegramBotCache, cls).__new__(cls)

        if chat_id not in cls.__instance.chat_messages:
            cls.__instance.chat_messages[chat_id] = ChatCache()

        return cls.__instance.chat_messages[chat_id]
