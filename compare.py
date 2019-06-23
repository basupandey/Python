num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the last number "))
if num1 > num2:
    if num1>num3:
        g=num1
    else:
        g=num2
else:
    if num2>num3:
        g=num2
    else:
        g=num3

print("The greatest number is:"+g)
print(type(num1))
