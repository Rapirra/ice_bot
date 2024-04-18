subQuery = """
           subscription Subscription {
  displayOrderToBot {
    deliveryBtns {
      id
      type
      event
      key
      color
    }
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
  }
}
"""

btnMutation = """
mutation DeliveryButton($order: Float, $button: Float) {
  deliveryButton(order: $order, button: $button) {
    id
      type
      event
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




