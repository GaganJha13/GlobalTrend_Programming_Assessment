def fibonacci_recursive(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 0  # Fibonacci sequence starts with 0, 1, 1, 2, 3, ...
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
# Example usage
n = 6
fibonacci_number = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is: {fibonacci_number}")
