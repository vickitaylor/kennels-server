EMPLOYEES = [
    {
        "id": 1,
        "name": "Sunny Riversounds"
    },
    {
        "id": 2,
        "name": "Butterfly Soulflight"
    }
]


def get_all_employees():
    """
    function gets all employees
    """
    return EMPLOYEES


def get_single_employee(id):
    """
    function gets a single employee by their id

    Args:
        id (int): the employee id

    Returns:
        dict: the single employee
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


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
