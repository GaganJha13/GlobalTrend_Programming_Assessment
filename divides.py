def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result
# Example usage
result1 = divide_numbers(10, 2)
print("Result:", result1)  # Output: Result: 5.0

result2 = divide_numbers(10, 0)
print("Result:", result2)  # Output: Error: Division by zero is not allowed.
