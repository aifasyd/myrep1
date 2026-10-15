n = int(input("Enter n: "))

evensum = 0
div = 0
prime = 0

for num in range(1, n + 1):

    if num % 2 == 0:
        evensum = evensum + num

    if num % 3 == 0 and num % 5 == 0:
        div = div + 1

    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            if num > prime:
                prime = num

    root = int(num ** 0.5)
    if root * root == num:
        digitsum = 0
        for digit in str(num):
            digitsum = digitsum + int(digit)
        print(num, "is a perfect square, digit sum =", digitsum)

print()
print("Sum of even numbers:", evensum)
print("Count divisible by both 3 and 5:", div)
print("Largest prime number:", prime)