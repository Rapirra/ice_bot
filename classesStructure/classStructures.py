from aiogram.fsm.state import StatesGroup, State


class BotMessage:
    user_token = ''
    objectMessage = {}
    deliveryBtns = {}
    user_me = {}
    order_related_messages = {}

    def adduser_token(self, user_token):
        self.user_token = user_token

    def add_order_related_message(self, message_id, order_id):
        if order_id in self.order_related_messages:
            self.order_related_messages[order_id].add(message_id)
        else:
            self.order_related_messages[order_id] = {message_id}

    def addObjMessage(self, objectMessage):
        obj_id = objectMessage['id']
        found_item = self.objectMessage.get(obj_id)
        if found_item:
            self.objectMessage.update({obj_id: objectMessage})
        else:
            self.objectMessage[obj_id] = objectMessage

    def getObjMessageById(self, obj_id):
        return self.objectMessage.get(obj_id)

    def add_user_me(self, user_me):
        self.user_me = user_me

    def add_delivery_btns(self, delivery_btns, order_id):
        found_item = self.deliveryBtns.get(order_id)
        if found_item is not None:
            self.deliveryBtns.update({order_id: delivery_btns})
        else:
            self.deliveryBtns[order_id] = delivery_btns

    def get_delivery_btns(self, order_id):
        return self.deliveryBtns.get(order_id)

    def clear(self):
        self.objectMessage = {}
        self.deliveryBtns = {}
        self.user_me = {}
        self.order_related_messages = {}


class RegisterMessage(StatesGroup):
    user_token = State()
    user_socket_me = State()
    chat_id = State()
    comment_request = State()
    comment_text = State()
    comment_handle = State()
    order_register_id = State()


botMessage = BotMessage()
