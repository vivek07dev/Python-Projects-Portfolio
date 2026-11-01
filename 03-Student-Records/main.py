Subjects = ("Python","Maths","DS")

student_data = {}
n_std = int(input("Enter the number of students: "))
for i in range(n_std):
    student_id = int(input("Enter student ID: "))
    name = input("Enter Name: ")
    python_marks = int(input("Enter Python marks: "))
    maths_marks = int(input("Enter Maths marks: "))
    ds_marks = int(input("Enter DS marks: "))
    print()

    
    student_data[student_id] = {
        "Name": name,
        "Python": python_marks,
        "Maths": maths_marks,
        "DS": ds_marks
    }

print("\nStudent Data:")


print("======STUDENT REPORT =======")



for student_id, data in student_data.items():
    
    print(f"{student_id} | {data['Name']}")

    print(f"Python: {data['Python']} | Maths: {data['Maths']} | DS: {data['DS']}")
    total_marks = data['Python'] + data['Maths'] + data['DS']
    average_marks = total_marks / len(Subjects)
    if average_marks >=75:
        result = "Distinction"
    elif average_marks >= 40:
        result = "Pass"

    else:

        
        result = "Fail"

    print(f"Total Marks: {total_marks} | Average Marks: {average_marks:.2f} | Result: {result}")
    print()

print("Student recorded:", len(student_data))