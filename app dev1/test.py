# Function to divide two numbers
def divide_numbers(num1, num2):
    try:
        # Perform the division
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Main function
def main():
    try:
        # Get input from the user
        number1 = float(input("Enter the numerator: "))
        number2 = float(input("Enter the denominator: "))
        
        # Calculate the result
        result = divide_numbers(number1, number2)
        
        # Display the result
        if isinstance(result, str):
            print(result)
        else:
            print(f"The result of {number1} divided by {number2} is {result}.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Execute the main function
if __name__ == "__main__":
    main()
