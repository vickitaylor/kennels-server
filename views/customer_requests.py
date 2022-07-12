CUSTOMERS = [
    {
        "id": 1,
        "name": "Sunshine Moonflight"
    },
    {
        "id": 2,
        "name": "Snowberry Willowwisp"
    }
]


def get_all_customers():
    """
    function gets all customers
    """
    return CUSTOMERS


def get_single_customer(id):
    """
    function gets a single customer by the id
    """
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    """
    function creates a new customer
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id +1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    """
    function deletes a single customer by the id
    """
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)