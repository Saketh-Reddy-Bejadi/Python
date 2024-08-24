def valid(s):
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        if stack:
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
    return len(stack) == 0
s = "()]"::
print(valid(s))