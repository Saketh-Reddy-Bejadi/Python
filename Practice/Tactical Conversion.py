for _ in range(int(input())):
    n=int(input())
    s=input()
    c=s.count('1')
    if c<=1:print('Yes')
    elif c==2:print('Yes' if '11' not in s else 'No')
    elif c==3:print('Yes' if '111' not in s else 'No')
    else:print('Yes')