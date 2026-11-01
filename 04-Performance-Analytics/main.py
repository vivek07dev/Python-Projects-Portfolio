# Performance Analytics System

student = {

    "vivek":89,
    "neeraj":75,
    "suraj":86,
    "rohit":85
}

# Display student marks

print("student performance analytics")

for name,marks in student.items():
    print(name,":",marks)

 # Calculate total marks

total = sum(student.values()) 
print("\ntotalmarks:,total")  

# Calculate Average marks

average = total/len(student)
print("avera marks:", average)

# Find highest marks
highest = marks(student,key=student.get)
print("highestmarks:",highest,"-",student(highest))

#find lowest marks
lowest = marks (student,key=student.get)
print("lowestmarks:",lowest,"-",student[lowest])

# chwck PASS AND FAIL

print("\npass/failResults:")

for name,marks in student.items():
    if marks>=50:
        print(name,"pass")
    else:

        print(name,"fail")

# performance analysis

print("\nPerformance Analysis: ")

for name, marks in student.item():
    if marks>=85:
        print(name,"Excellent")

    if marks>=65:
        print(name,"Good")   

    if marks>=40:
        print(name,"Average")  

    else:
        print(name,"Needs Improvement")





