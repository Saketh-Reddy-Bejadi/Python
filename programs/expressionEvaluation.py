# def evaluate_postfix(expression):
#     stack = []
#     operators = {'+': lambda x, y: x + y,
#                  '-': lambda x, y: x - y,
#                  '*': lambda x, y: x * y,
#                  '/': lambda x, y: x / y}

#     for char in expression:
#         if char.isdigit():
#             stack.append(int(char))
#         elif char in operators:
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             result = operators[char](operand1, operand2)
#             stack.append(result)

#     return stack.pop()


# # Example usage
# postfix_expression = input("Enter a postfix expression: ")
# result = evaluate_postfix(postfix_expression)
# print("Result:", result)


def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)
        else:
            raise ValueError("Invalid token: " + token)

    if len(stack) == 1:
        return stack.pop()
    else:
        raise ValueError("Invalid expression")

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    
expression = "42 3 1 * + 9 -"
result = evaluate_postfix(expression)
print("Result:", result)
