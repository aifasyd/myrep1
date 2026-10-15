category = input("Enter category (commercial/non-commercial): ").lower()
units = float(input("Enter units consumed: "))


bill = 0

if category == "commercial":
    rate1 = 10
    rate2 = 12
    rate3 = 15
else:
    rate1 = 5
    rate2 = 6
    rate3 = 8

remaining = units

if remaining <= 100:
    bill = remaining * rate1
    remaining = 0
else:
    bill = 100 * rate1
    remaining = remaining - 100

    if remaining <= 300:
        bill = bill + remaining * rate2
        remaining = 0
    else:
        bill = bill + 300 * rate2
        remaining = remaining - 300
        bill = bill + remaining * rate3

print("Category:", category)
print("Units Consumed:", units)
print("Final Bill:", bill)