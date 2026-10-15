def read_data():
    name = input("Enter name: ")
    roll_no = int(input("Roll number: "))
    python = int(input("Python marks: "))
    math = int(input("Math marks: "))
    dbms = int(input("DBMS marks: "))
    return name, roll_no, python, math, dbms

def total_marks(python, math, dbms):
    total = python + math + dbms
    print("Total:", total)
    return total

def get_average(total):
    average = total / 3
    print("Average:", average)
    return average

def get_percentage(total):
    percentage = total / 300 * 100
    print("Percentage:", percentage)
    return percentage

def find_grade(percentage):
    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First class")
    elif percentage > 40:
        print("Second class")
    else:
        print("Fail")

for i in range(1, 4):
    print(f"\n--- Student {i} ---")
    
    name, roll_no, python, math, dbms = read_data()
    total = total_marks(python, math, dbms)
    av = get_average(total)
    percent = get_percentage(total)
    find_grade(percent)