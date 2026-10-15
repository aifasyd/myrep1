num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

print("Addition      :", num1 + num2)
print("Subtraction   :", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 == 0:
    print("Error: Division by zero is not allowed")
else:
    print("Division      :", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus       :", num1 % num2)

print("Exponentiation:", num1 ** num2)