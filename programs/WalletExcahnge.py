t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a==b:
        print("Bob")
    elif a>b:
        print("Bob")
    else:
        print("Alice")