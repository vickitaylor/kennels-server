import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Sunshine Moon"
    },
    {
        "id": 2,
        "name": "Snowberry Wisp"
    }
]


def get_all_customers():
    """
    Gets all customers from the database

    Returns:
        string: JSON serialized string of the contents of the customer table
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    return json.dumps(customers)


def get_single_customer(id):
    """
    Gets the requested customer from the database

    Args:
        id (int): The id of the requested customer

    Returns:
        string: JSON serialized string of the customer from the database
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address, 
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'],
                            data['address'], data['email'], data['password'])

        return json.dumps(customer.__dict__)


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


def get_customers_by_email(email):
    """
    Gets the customers by their email

    Args:
        email (string): The email is from teh query params of the request

    Returns:
        string: JSON serialized sting of the data
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
