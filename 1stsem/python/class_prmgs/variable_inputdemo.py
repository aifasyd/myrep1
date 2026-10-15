num1=int(input("enter the first num: "))
num2=int(input("enter the second num: "))

sum=num1+num2
diff=num1-num2
multp=num1*num2
rem=num1%num2
div=num1/num2
floor=num1//num2

print("the sum of",num1,"and",num2,"is",sum)
print("the difference of",num1,"and",num2,"is",diff)
print("the product of",num1,"and",num2,"is",multp)
print(f"the quotient of {num1} and {num2} is {div}")
print(f"the reminder of {num1} and {num2} is {rem}")
print(f"the rounded/int quotient value of {num1} and {num2} is {floor}")