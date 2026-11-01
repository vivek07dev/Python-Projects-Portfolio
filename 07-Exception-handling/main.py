import json
import os
from datetime import datetime
class StudentRecordError(Exception):
    pass
def validate_student(student):
    if not isinstance(student, dict):
        raise TypeError("Student record must be a dictionary")
    required_fields = [
        "student_id",
        "name",
        "department",
        "marks"
    ]
    for field in required_fields:
        if field not in student:
            raise KeyError(f"Missing required field '{field}'")
    if not isinstance(student["student_id"], str):
        raise TypeError("Student ID must be a string")
    if not isinstance(student["name"], str):
        raise TypeError("Name must be a string")
    if not isinstance(student["department"], str):
        raise TypeError("Department must be a string")
    if not isinstance(student["marks"], list):
        raise TypeError("Marks must be a list")
    if not student["student_id"].strip():
        raise ValueError("Student ID cannot be empty")
    if not student["name"].strip():
        raise ValueError("Student name cannot be empty")
    if not student["department"].strip():
        raise ValueError("Department cannot be empty")
    marks = student["marks"]
    if len(marks) != 3:
        raise StudentRecordError(
            "Marks must contain exactly 3 values"
        )
    for mark in marks:
        if isinstance(mark, bool):
            raise StudentRecordError(
                "Boolean values are not allowed as marks"
            )
        if not isinstance(mark, (int, float)):
            raise TypeError("Marks must be numeric values")
        if not 0 <= mark <= 100:
            raise StudentRecordError(
                "Marks must be between 0 and 100"
            )
    return student
def import_students(input_path):
    valid_students = []
    errors = []
    seen_ids = set()

    print("Import started:", input_path)
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            students = json.load(file)
    except FileNotFoundError:
        errors.append("Error: Input file not found")
        print("Error: Input file not found")
        return
    except PermissionError:
        errors.append("Error: Permission denied")
        print("Error: Permission denied")
        return
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON format: {e}")
        print("Error: Invalid JSON format")
        return
    except OSError as e:
        errors.append(f"File error: {e}")
        print("File error:", e)
        return
    except UnicodeDecodeError as e:
        errors.append(f"File encoding error: {e}")
        print("File encoding error:", e)
        return
    else:
        if not isinstance(students, list):
            errors.append("Error: JSON data must be a list")
            print("Error: JSON data must be a list")
            return
        for index, student in enumerate(students, start=1):
            try:
                validate_student(student)
                student_id = student["student_id"]
                if student_id in seen_ids:
                    raise StudentRecordError(
                        f"Duplicate student ID: {student_id}"
                    )
                seen_ids.add(student_id)
                valid_students.append(student)
                print(
                    f"Accepted: {student_id} - {student['name']}"
                )
            except StudentRecordError as e:
                message = f"Rejected record {index}: {e}"
                errors.append(message)
                print(message)
            except KeyError as e:
                message = f"Rejected record {index}: Missing field {e}"
                errors.append(message)
                print(message)
            except TypeError as e:
                message = f"Rejected record {index}: {e}"
                errors.append(message)
                print(message)
            except ValueError as e:
                message = f"Rejected record {index}: {e}"
                errors.append(message)
                print(message)
            except IndexError as e:
                message = f"Rejected record {index}: {e}"
                errors.append(message)
                print(message)
        with open(
            "students_valid.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                valid_students,
                file,
                indent=4
            )

        print("\nValid records saved successfully.")

    finally:

        print("\nImport process finished.")

    # Write error log
    try:

        with open(
            "import_errors.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                f"Import Error Report\n"
                f"Date: {datetime.now()}\n\n"
            )

            for error in errors:
                file.write(error + "\n")

    except OSError as e:

        print("Unable to write error log:", e)
        return

    # Final summary
    print("\nImport completed.")

    print("Accepted records:", len(valid_students))

    print("Rejected records:", len(errors))

    print("Valid output: students_valid.json")

    print("Error log: import_errors.txt")
if __name__ == "__main__":

    input_path = input(
        "Enter input file path (press Enter for default): "
    )

    if input_path.strip() == "":
        input_path = "students_input.json"

    import_students(input_path)