def add(a,b):
    return a+b
def subtract(a1,b1):
    return a1 - b1
def multiply(a,b):
    return a*b
def divide(a,b):
    return a / b
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
def calc():
    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)
    shouldContinue = True
    while shouldContinue:
        operationsSymb = input("Choose what operation you would like to perform: ")
        num2 = float(input("Enter the next number: "))
        calcFunction = operations[operationsSymb]
        answer = calcFunction(num1, num2)
        print(f"{num1} {operationsSymb} {num2} = {answer}")

        continuing = input(f"Type y to continue calculation with {answer}, or type n to exit.: ").lower()
        if continuing == "y":
            num1 = answer
        elif continuing == "n":
            shouldContinue = False
            calc()
calc()
