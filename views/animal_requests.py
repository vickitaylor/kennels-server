ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_animals():
    """ function gets all animals """
    return ANIMALS


def get_single_animal(id):
    """
    function looks up a single animal by the id, has a single parameter
    """
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the for..of loops in JavaScript
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


def create_animal(animal):
    """
    function to post a new animal to the list
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
    function that deletes an animal by their id
    """
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you can access
    # the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index

    # If the animal was found, use pop(int) to remove it from the list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)
