def calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2

def main():
    while True:
        operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")

        if operator.lower() == "q":
            print("Calculator closed")
            break
        if operator not in ("+", "-", "*", "/"):
            print("Invalid operator. Please try again.")
            continue

        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            result = calculator(number1, number2, operator)
            print("Result: ", result)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
if __name__ == "__main__":
    main()