

query = """
    query OrderToBot {
  orderToBot {
    id
    client {
      id
      name
    }
    more {
      id
      views
      urgently
      date_ready
      date_closed
      discount
      notes
      recommendation
    }
    name
    paid
    price
    parent
    status {
      id
      name
    }
  }
}
"""






