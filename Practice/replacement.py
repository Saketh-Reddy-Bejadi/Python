def func(n,s1,s2):
    str1=[]
    d=0
    for i in s1:
        str1.append(i)
        while(len(str1)>=2 and str1[-2]!=str1[-1] and d<len(s2)):
            r=s2[d]
            str1.pop()
            str1.pop()
            str1.append(r)
            d+=1
    print('YES' if (d==n-1 and len(str1)==1) else 'NO')

for _ in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()
    func(n,s1,s2)