def valid(t,s):
    for i in range(len(t)):
        for j in range(0, len(t) - i - 1):
            if t[j][1] < t[j + 1][1]:
                t[j], t[j + 1] = t[j + 1], t[j]
    b=0
    for i in t:
        if i[0]<=s:
            b+=i[0]*i[1]
            s-=i[0]
        else:
            while(s>0):
                s-=1
                b+=1*i[1]
    return b
            
    
print(valid([[5,10],[2,5],[4,7],[3,9]],10))