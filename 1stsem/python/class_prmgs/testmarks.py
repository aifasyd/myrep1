# Student 1
name1 = input("Enter first student name: ")
python1 = float(input("Enter Python mark: "))
english1 = float(input("Enter English mark: "))
maths1 = float(input("Enter Maths mark: "))

total1 = python1 + english1 + maths1
average1 = total1 / 3

# Student 2
name2 = input("Enter second student name: ")
python2 = float(input("Enter Python mark: "))
english2 = float(input("Enter English mark: "))
maths2 = float(input("Enter Maths mark: "))

total2 = python2 + english2 + maths2
average2 = total2 / 3

# Table
print()
print(f"{'NAME':<20} {'PYTHON':<11} {'ENG':<11} {'MATHS':<11} {'TOTAL':<11} {'AVG%':<11}")
print("-" * 75)
print(f"{name1[:18]:<20} {python1:<11} {english1:<11} {maths1:<11} {total1:<11} {round(average1,1)}")
print(f"{name2[:18]:<20} {python2:<11} {english2:<11} {maths2:<11} {total2:<11} {round(average2,1)}")