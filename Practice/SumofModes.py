def countM(s):
    co=[0,0]
    for char in s:
        co[int(char)]+=1
    mc=max(co)
    m=[]
    for i,freq in enumerate(co):
        if freq==mc:
            m.append(i)
    return len(m)

for _ in range(int(input())):
    lenOfstr=int(input())
    string=input()
    co={}
    mc=0
    result=0
    for i in range(lenOfstr):
        for j in range(i,lenOfstr):
            for char in string:
                co[char]=co.get(char,0)+1
            mc=max()
    print(result)