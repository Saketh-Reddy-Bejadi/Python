def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    return armstrong_sum == number

num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
