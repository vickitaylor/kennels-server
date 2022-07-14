import sqlite3
import json
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]


def get_all_locations():
    """
    Gets all locations from the database

    Returns:
        string: JSON serialized string of the contents of the location table
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return json.dumps(locations)


def get_single_location(id):
    """
    Gets the requested location from the database

    Args:
        id (int): The id of the requested location

    Returns:
        string: JSON serialized string of the location from the database
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

def create_location(location):
    """
    Function that adds an new location to the list

    Args:
        location (dict): The new location to be added

    Returns:
        dict: The location that was added with its new id
    """
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location


def delete_location(id):
    """
    Removes the selected location from the list

    Args:
        id (int): The id of the location to be deleted
    """
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, updated_location):
    """
    Updates a single location in the database

    Args:
        id (int): The id of the location
        updated_location (dict): The updated location dictionary
    """
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = updated_location
            break
