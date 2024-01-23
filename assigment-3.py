
def factorial(num):
    factorial=1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        

    return factorial

def divide(num1,num2):
    q=num1//num2

    return q


ch = input("Enter any of these char for specific operation !,*,/: ")

result = 0
if ch == '!':
    num1 = int(input("Enter Number: "))
    result = factorial(num1)

elif ch == '*':
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 * num2

elif ch == '/':
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = divide(num1,num2)
else:
    print("Input character is not recognized!")

if ch == '!':
    print("The factorial of",num1,"is",result)
else:
    print(num1 , ch , num2 ,':',result )