def divide_numbers(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return dividend / divisor

try:
    dividend=int(input("Enter divident:"))
    divisor=int(input("Enter divisior:"))
    result = divide_numbers(dividend,divisor)
    print("Result:", result)
except ValueError as e:
    print("Error:", str(e))
