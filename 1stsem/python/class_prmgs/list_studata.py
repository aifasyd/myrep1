def read_student():
    name = input("Enter name: ")
    roll_no = int(input("Enter roll number: "))
    mobile = input("Enter mobile number: ")
    email = input("Enter email: ")

    marks = []
    for i in range(5):
        m = int(input("Enter marks in subject " + str(i + 1) + ": "))
        marks.append(m)

    student = [name, roll_no, mobile, email, marks]
    return student


def get_total(marks):
    total = 0
    for m in marks:
        total = total + m
    return total


def add_total(student):
    total = get_total(student[4])
    student.append(total)


def display_student(student, number):
    marks = student[4]

    print("\n------ Student", number, "------")
    print("Name    :", student[0])
    print("Roll No :", student[1])
    print("Mobile  :", student[2])
    print("Email   :", student[3])
    for i in range(len(marks)):
        print("Subject", i + 1, ":", marks[i])
    print("Total   :", student[5])


def display_all(student_list):
    print("\n===== Student List =====")
    print(student_list)

    for i in range(len(student_list)):
        display_student(student_list[i], i + 1)


n = int(input("How many students? "))

if n <= 0:
    print("Error: Number of students must be greater than zero")
else:
    student_list = []

    for i in range(n):
        print("\nEnter details of student", i + 1)
        student = read_student()
        add_total(student)
        student_list.append(student)

    display_all(student_list)