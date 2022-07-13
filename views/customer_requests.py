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
    Function that adds an new customer to the list

    Args:
        customer (dict): The new customer to be added

    Returns:
        dict: The customer that was added with its new id
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer


def delete_customer(id):
    """
    Removes the selected customer from the list

    Args:
        id (int): The id of the customer to be deleted
    """
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, updated_customer):
    """
    updates a single customer in the database

    Args:
        id (int): the id of the customer to be updated
        updated_customer (dict): The updated customer dictionary
    """
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = updated_customer
            break
