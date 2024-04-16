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
}"""





