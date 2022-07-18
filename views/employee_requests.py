import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Sunny River"
    },
    {
        "id": 2,
        "name": "Butterfly Soul"
    }
]


def get_all_employees():
    """
    Gets all employees from the database

    Returns:
        string: JSON serialized string of the contents of the employee table
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
	        e.id,
	        e.name,
	        e.address,
	        e.location_id,
	        l.name location_name,
	        l.address location_address
        FROM Employee e
        JOIN Location l
	        ON l.id = e.location_id;
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])

            location = Location(
                row['id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return json.dumps(employees)


def get_single_employee(id):
    """
    Gets the requested employee from the database

    Args:
        id (int): The id of the requested employee

    Returns:
        string: JSON serialized string of the employee from the database
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'],
                            data['address'], data['location_id'])

        return json.dumps(employee.__dict__)


def create_employee(employee):
    """
    Function adds a new employee to the list

    Args:
        employee (dict): The new employee to be added

    Returns:
        dict: The employee that was added and its new id
    """
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee


def delete_employee(id):
    """
    Removes a single employee from the list by their id

    Args:
        id (int): The id of the employee to be deleted
    """
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, updated_employee):
    """
    Updates a single employee in the database

    Args:
        id (int): The id of the employee
        updated_employee (dict): The updated employee dictionary
    """
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = updated_employee
            break


def get_employees_by_location(location_id):
    """
    Gets the employees by the location id

    Args:
        location_id (int): The location id from the query params of the request

    Returns:
        Serialized sting of the data
    """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
