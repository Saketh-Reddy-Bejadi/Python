for _ in range(int(input())):
    s=input().strip()
    if s==s[::-1]:
        print("NO")
    else:
        print("YES")
        print(s[::-1])