subQuery = """
     subscription Subscription {
  displayOrderToBot {
    order {
      id
      name
      client {
        addresses {
          address
        }
        id
        name
        numbers {
          phone
        }
      }
      status {
        more {
          delivery
        }
      }
    }
    deliveryBtns {
      id
      type
      frontEvent
      backEvent
      key
      color
    }
  }
}
"""

btnMutation = """
mutation DeliveryButton($order: Float, $button: Float) {
  deliveryButton(order: $order, button: $button) {
   id
    type
    frontEvent
    backEvent
    key
    color
  }
}
"""

commentMutation = """
mutation Mutation($module: CRMModules, $comment: String, $object: Float) {
  comment(module: $module, comment: $comment, object: $object) {
    id
  }
}
"""

meQuery = """
query Query {
  me {
    name
    id
  }
}
"""





