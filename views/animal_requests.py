import sqlite3
import json
from models import Animal, Location, Customer


ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "location": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    """
    Gets all animals from the database

    Returns:
        string: JSON serialized string of the contents of the animal table
    """

    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It is a black box
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
	        a.id,
	        a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
	        c.name customer_name, 
	        c.address customer_address,
	        c.email customer_email,
	        c.password customer_password
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
	        ON c.id = a.customer_id 
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from the database
        for row in dataset:

            # Create an animal instance from the current row.  Note that the database fields are
            # specified in exact order of the parameters defined in teh Animal class above
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])

            # Create a Location instance from the current row
            location = Location(
                row['id'], row['location_name'], row['location_address'])

            # Creating a Customer instance
            customer = Customer(
                row['id'], row['customer_name'], row['customer_address'], row['customer_email'],
                row['customer_password'])

            # Add the dictionary representation of the location/customer to the animal
            animal.location = location.__dict__
            animal.customer = customer.__dict__

            # Add the dictionary representation of the animal to the list
            animals.append(animal.__dict__)

    # Use 'json' package to properly serialize list as JSON
    return json.dumps(animals)


def get_single_animal(id):
    """
    Gets the requested animal from the database

    Args:
        id(int): The id of the requested animal

    Returns:
        string: JSON serialized string of the animal from the database
    """

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable value into the SQL statement
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id= ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'], data['customer_id'])

        return json.dumps(animal.__dict__)


def create_animal(animal):
    """
    Function that adds an new animal to the list

    Args:
        animal(dict): The new animal to be added

    Returns:
        dict: The animal that was added with its new id
    """
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an "id" property to the animal directory
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with "id" property added
    return animal


def delete_animal(id):
    """
    Removes the selected animal from the list

    Args:
        id(int): The id of the animal to be deleted
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE from animal
            WHERE id= ?
            """, (id, ))


def update_animal(id, updated_animal):
    """
    Updates a single animal in the database

    Args:
        id(int): The id of the animal
        updated_animal(dict): The updated animal dictionary
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name= ?,
                breed= ?,
                status= ?,
                location_id= ?,
                customer_id= ?
        WHERE id= ?
        """, (updated_animal['name'], updated_animal['breed'], updated_animal['status'],
              updated_animal['locationId'], updated_animal['customerId'], id, ))

        # Were any rows affected?
        # Did the client send an 'id' that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def get_animals_by_location(location_id):
    """
    Gets the animal by the location id

    Args:
        location_id(int): The location id from the query params of the request

    Returns:
        Serialized sting of the data
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.location_id= ?
        """, (location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def get_animals_by_status(status):
    """
    Gets the animal by the status

    Args:
        status(string): The status from the query params of the request

    Returns:
        Serialized sting of the data
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.status= ?
        """, (status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)
