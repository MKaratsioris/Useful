from flask import jsonify

def validate_employee_data(data, required_fields):
    """
    Validates required fields in the incoming JSON data.
    """
    missing = [field for field in required_fields if field not in data]
    if missing:
        return False, jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    if "salary" in data:
        try:
            data["salary"] = int(data["salary"])
        except ValueError:
            return False, jsonify({"error": "Salary must be an integer"}), 400

    return True, data, None
