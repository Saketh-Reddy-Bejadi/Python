def find_values(num):
    n = len(num)
    for i in range(1, n):
        a_str = num[:i]
        b_str = num[i:]
        
        a = int(a_str)
        b = int(b_str)
        
        if a_str[0] != '0' and b_str[0] != '0' and b > a:
            return a, b

    return -1, -1

t = int(input())
for _ in range(t):
    num = input()
    num1, num2 = find_values(num)
    if num1 == -1:
        print(-1)
    else:
        print(num1, num2)
