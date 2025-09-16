def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
        return x / y
def main():
    print("Simple Calculator")
    print("Operation: + - * /")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")
            if operator.lower() == 'q':
                print("Exiting the calculator. Goodbye!")
                break
            num2 = float(input("Enter second number: "))
            if operator == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operator == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operator == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operator == '/':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid operator. Please try again.")
                continue
                print(f"Result: {result}")
        except ValueError:
            print("please enter valid number.")
        again=input("Do another calculation? (y/n):").lower()
        if again!='y':
            print("Goodbye")
            break
if __name__ == "__main__":
    main()

   