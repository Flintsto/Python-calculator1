# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

# Main function to handle user input and display results
def main():
    print("Welcome to the FranCee Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Enter 'exit' to quit")
    print("You can use multiple operators in a single expression.")

    while True:
        try:
            # Get user input for operation
            operation_choice = input("Select operation (1/2/3/4): ")

            # Check if the user wants to exit
            if operation_choice.lower() == 'exit':
                print("Thank you for using the FranCee Calculator. Goodbye!")
                break

            operation_choice = int(operation_choice)

            # Get user input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the selected operation
            if operation_choice == 1:
                result = add(num1, num2)
            elif operation_choice == 2:
                result = subtract(num1, num2)
            elif operation_choice == 3:
                result = multiply(num1, num2)
            elif operation_choice == 4:
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please select a valid operation.")
                continue

            print("Result:")
            print(int(result))

        except Exception as e:
            print("Error: ", e)

# Run the calculator
if __name__ == "__main__":
    main()

