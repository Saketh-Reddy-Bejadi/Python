def valid(s):
    stack = []
    c = 0
    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if (
                not stack
                or (char == ")" and stack[-1] != "(")
                or (char == "}" and stack[-1] != "{")
                or (char == "]" and stack[-1] != "[")
            ):
                return False
            stack.pop()
    return not stack


s = "()"
print(valid(s))
