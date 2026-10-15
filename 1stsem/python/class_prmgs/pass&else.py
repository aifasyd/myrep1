name = ''
roll_no = 0
python = 0
math = 0
dbms = 0
total = 0
percentage = 0

def read_data():
    global name, roll_no, python, math, dbms
    name = input("Enter name: ")
    roll_no = int(input("Roll number: "))
    python = int(input("Python marks: "))
    math = int(input("Math marks: "))
    dbms = int(input("DBMS marks: "))

def total_marks():
    global total
    total = python + math + dbms
    print("Total:", total)

def get_average():
    global total
    average = total / 3
    print("Average:", average)

def get_percentage():
    global percentage
    percentage = total / 300 * 100
    print("Percentage:", percentage)

def find_grade():
    global percentage
    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First class")
    elif percentage > 40:
        print("Second class")
    else:
        print("Fail")

def main():
    num_students = 3
    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        read_data()
        total_marks()
        get_average()
        get_percentage()
        find_grade()

main()