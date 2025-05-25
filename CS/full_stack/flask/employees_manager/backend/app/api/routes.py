from flask import Blueprint, request, jsonify, current_app
from app.models.employee import Employee
from app.api.utils import validate_employee_data

bp = Blueprint("api", __name__)

@bp.route("/employees", methods=["GET"])
def get_all_employees():
    """
    Get all employees
    ---
    tags:
      - Employees
    responses:
      200:
        description: A list of all employees
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  first_name:
                    type: string
                  last_name:
                    type: string
                  salary:
                    type: integer
              example:
                - first_name: John
                  last_name: Doe
                  salary: 80000
                - first_name: Jane
                  last_name: Doe
                  salary: 90000
      500:
        description: Internal server error
        content:
          application/json:
            schema:
              type: object
              example:
                error: Internal Server Error
    """
    db = current_app.get_db()
    current_app.logger.info("Received request to fetch all employees")

    try:
        employees = db.show_all()
        employees_data = [
            {"first_name": e[0], "last_name": e[1], "salary": e[2]} for e in employees
        ]
        current_app.logger.info(f"Fetched {len(employees)} employee(s) from database")
        return jsonify(employees_data), 200
    except Exception as e:
        current_app.logger.error(f"Failed to fetch all employees: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@bp.route("/employee", methods=["POST"])
def create_employee():
    """
    Create a new employee
    ---
    tags:
      - Employees
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - first_name
              - last_name
              - salary
            properties:
              first_name:
                type: string
              last_name:
                type: string
              salary:
                type: integer
            example:
              first_name: John
              last_name: Doe
              salary: 80000
    responses:
      201:
        description: Employee created successfully
        content:
          application/json:
            schema:
              type: object
              example:
                message: Employee created
      400:
        description: Invalid input data
        content:
          application/json:
            schema:
              type: object
              example:
                error: Invalid input
      500:
        description: Internal server error
        content:
          application/json:
            schema:
              type: object
              example:
                error: Internal Server Error
    """
    db = current_app.get_db()
    data = request.get_json()

    current_app.logger.info("Received request to create an employee")

    is_valid, validated_data, error_response = validate_employee_data(data, ["first_name", "last_name", "salary"])
    if not is_valid:
        current_app.logger.warning(f"Validation failed for create_employee: {error_response[0].json}")
        return error_response

    try:
        emp = Employee(**validated_data)
        db.insert(emp)
        current_app.logger.info(f"Inserted employee: {emp.full_name}")
        return jsonify({"message": "Employee added"}), 201
    except Exception as e:
        current_app.logger.error(f"Failed to insert employee: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@bp.route("/employee/<last_name>", methods=["GET"])
def get_employees_by_last_name(last_name):
    """
    Get all employees with a given last name
    ---
    tags:
      - Employees
    parameters:
      - name: last_name
        in: path
        required: true
        schema:
          type: string
    responses:
      200:
        description: List of matching employees
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  first_name:
                    type: string
                  last_name:
                    type: string
                  salary:
                    type: integer
              example:
                - first_name: John
                  last_name: Doe
                  salary: 80000
                - first_name: Jane
                  last_name: Doe
                  salary: 90000
      500:
        description: Internal server error
        content:
          application/json:
            schema:
              type: object
              example:
                error: Internal Server Error
    """
    db = current_app.get_db()

    current_app.logger.info(f"Fetching employees with last name: {last_name}")

    try:
        employees = db.get_employees_last_name(last_name.capitalize())
        employees_data = [
            {"first_name": e[0], "last_name": e[1], "salary": e[2]} for e in employees
        ]
        current_app.logger.info(f"Found {len(employees)} employee(s) with last name {last_name}")
        return jsonify(employees_data), 200
    except Exception as e:
        current_app.logger.error(f"Error retrieving employees: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@bp.route("/employee/salary", methods=["PUT"])
def update_employee_salary():
    """
    Update an employee's salary
    ---
    tags:
      - Employees
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - first_name
              - last_name
              - salary
            properties:
              first_name:
                type: string
              last_name:
                type: string
              salary:
                type: integer
            example:
              first_name: John
              last_name: Doe
              salary: 100000
    responses:
      200:
        description: Salary updated successfully
        content:
          application/json:
            schema:
              type: object
              example:
                message: Salary updated
      400:
        description: Invalid input
        content:
          application/json:
            schema:
              type: object
              example:
                error: Invalid input
      500:
        description: Internal Server Error
        content:
          application/json:
            schema:
              type: object
              example:
                error: Internal Server Error
    """
    db = current_app.get_db()
    data = request.get_json()

    current_app.logger.info("Received request to update employee salary")

    is_valid, validated_data, error_response = validate_employee_data(data, ["first_name", "last_name", "salary"])
    if not is_valid:
        current_app.logger.warning(f"Validation failed for update_employee_salary: {error_response[0].json}")
        return error_response

    try:
        emp = Employee(validated_data["first_name"], validated_data["last_name"], 0)
        db.update_salary(emp, validated_data["salary"])
        current_app.logger.info(f"Updated salary for: {emp.full_name} to {validated_data['salary']}")
        return jsonify({"message": "Salary updated"}), 200
    except Exception as e:
        current_app.logger.error(f"Failed to update salary: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@bp.route("/employee", methods=["DELETE"])
def delete_employee():
    """
    Delete an employee
    ---
    tags:
      - Employees
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - first_name
              - last_name
            properties:
              first_name:
                type: string
              last_name:
                type: string
            example:
              first_name: John
              last_name: Doe
    responses:
      200:
        description: Employee deleted successfully
        content:
          application/json:
            schema:
              type: object
              example:
                message: Employee deleted
      400:
        description: Invalid input
        content:
          application/json:
            schema:
              type: object
              example:
                error: Invalid input
      500:
        description: Internal Server Error
        content:
          application/json:
            schema:
              type: object
              example:
                error: Internal Server Error
    """
    db = current_app.get_db()
    data = request.get_json()

    current_app.logger.info("Received request to delete employee")

    is_valid, validated_data, error_response = validate_employee_data(data, ["first_name", "last_name"])
    if not is_valid:
        current_app.logger.warning(f"Validation failed for delete_employee: {error_response[0].json}")
        return error_response

    try:
        emp = Employee(validated_data["first_name"], validated_data["last_name"], 0)
        db.remove_employee(emp)
        current_app.logger.info(f"Deleted employee: {emp.full_name}")
        return jsonify({"message": "Employee deleted"}), 200
    except Exception as e:
        current_app.logger.error(f"Failed to delete employee: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
