#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.#
#5Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.#
#
num1=eval(input("Enter the first integer:"))
num2=eval(input("Enter the second integer:"))
operation=(input("Enter operation(+,-,*,/:"))
#operations
if operation == "+" :
    result= num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-" :
    result= num1-num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*"  :
    result= num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error!!!!!!!!!!!!! Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")


