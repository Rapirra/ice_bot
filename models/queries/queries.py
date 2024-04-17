subQuery = """
    subscription Subscription {
  displayOrderToBot {
    deliveryBtns {
      id
      static
      button {
        id
        type
        event
        color
        key
      }
      comment
      score
      type
      parent
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
      event
      color
    key
    type
  }
}
"""




