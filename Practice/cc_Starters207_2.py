for _ in range(int(input())):
    n=int(input())
    s=input()
    l=s.find('1')
    h=s.rfind('1')
    print(s[l:h+1].count('0'))