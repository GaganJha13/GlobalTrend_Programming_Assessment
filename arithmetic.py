def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError(f"Invalid operator '{operator}'. Supported operators are '+', '-', '*', '/'.")


num1 = 10
num2 = 5
operator = '+'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

operator = '-'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

operator = '*'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

operator = '/'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")
