category = input("Enter category (commercial/non-commercial): ")
unit = float(input("Enter units consumed: "))

bill = 0

if category == "commercial":
    rate1 = 10
    rate2 = 12
    rate3 = 15
else:
    rate1 = 5
    rate2 = 6
    rate3 = 8

remaining = int(unit)

if remaining < 100:
    part1 = remaining % 100
else:
    part1 = 100

remaining = remaining - part1

if remaining < 300:
    part2 = remaining % 300
else:
    part2 = 300

remaining = remaining - part2

part3 = remaining

bill = part1 * rate1 + part2 * rate2 + part3 * rate3

print("Category:", category)
print("Units Consumed:", unit)
print("Final Bill:", bill)