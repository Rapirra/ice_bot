class ChatCache:
    def __init__(self):
        self.user_token = ''
        self.objectMessage = {}
        self.deliveryBtns = {}
        self.user_me = {}
        self.order_related_messages = {}

    def adduser_token(self, user_token):
        self.user_token = user_token

    def add_order_related_message(self, message_id, order_id):
        if order_id in self.order_related_messages:
            self.order_related_messages[order_id].append(message_id)
        else:
            self.order_related_messages[order_id] = [message_id]

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

    def delete_msg_from_dict(self, order_id):
        order_set = self.order_related_messages.get(order_id)
        if order_set:
            order_set.clear()
            if not order_set:
                del self.order_related_messages[order_id]

    def clear(self):
        self.objectMessage = {}
        self.deliveryBtns = {}
        self.user_me = {}
        self.order_related_messages = {}

