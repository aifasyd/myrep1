def get_marks(subject):
    while True:
        marks = int(input(f"Enter marks in {subject} (0-100): "))
        if 0 <= marks <= 100:
            return marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

m1 = get_marks("Subject 1")
m2 = get_marks("Subject 2")
m3 = get_marks("Subject 3")

total = m1 + m2 + m3
average = round(total / 3, 3)
percentage = round((total / 300) * 100, 3)

print("Total     :", total)
print("Average   :", average)
print("Percentage:", percentage)

if percentage >= 70:
    print("Grade: DISTINCTION")
elif percentage >= 60:
    print("Grade: FIRST CLASS")
elif percentage >= 40:
    print("Grade: SECOND CLASS")
else:
    print("Grade: FAIL")