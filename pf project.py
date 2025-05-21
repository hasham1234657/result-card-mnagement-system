# Function to take student data
def get_student_data():
    name = input("Student Name: ")
    subjects = ["Math", "Science", "English"]
    marks = {}

    for subject in subjects:
        score = int(input(f"{subject} ke marks daalain: "))
        marks[subject] = score

    return {"name": name, "marks": marks}

# Function to calculate average marks
def calculate_average(marks):
    total = sum(marks.values())
    average = total / len(marks)
    return average

# Function to calculate grade based on average
def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

# Function to print report card
def print_report_card(student):
    print("\n--- Report Card ---")
    print("Naam:", student["name"])
    for subject, score in student["marks"].items():
        print(f"{subject}: {score}")
    avg = calculate_average(student["marks"])
    grade = get_grade(avg)
    print("Average Marks:", avg)
    print("Grade:", grade)
    print("-------------------")

# Main program
students = []

num_students = int(input("number of student record? "))

for _ in range(num_students):
    student = get_student_data()
    students.append(student)

    print_report_card(student)