for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    i=1
    while(i<n):
        if s[i] == s[i-1]:
            c += 1
            i+=2
        else:
            i+=1
    print(n - c)