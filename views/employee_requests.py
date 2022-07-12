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
    function gets a single employee by the id
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    """
    function creates a new employee
    """
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    """
    function that will delete an employee by the id
    """
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
        
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)