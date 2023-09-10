def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

infix_expression = input("Enter an infix expression: ")
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)


