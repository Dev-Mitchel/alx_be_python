def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number here: "))
    num2 = float(input("Enter the second number here: "))
    operation = str(input("Choose an operstion(add, subtract, multiply or divide): ")).strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    elif operation == "divide" and num2 == 0:
        print("Invalid input!")
