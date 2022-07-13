
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
    function gets all locations
    """
    return LOCATIONS


def get_single_location(id):
    """
    function gets a single location by the id
    """
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location


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
