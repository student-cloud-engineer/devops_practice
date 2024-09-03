def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
numbers = [2, 3, 4, 5]  # List of numbers to multiply
product = multiply_numbers(numbers)
print(f"The product of the numbers is: {product}")
