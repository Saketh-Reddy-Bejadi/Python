def valid(count, temp ,noOf):
    for i in range(1,2*noOf):
        if temp[i]>=temp[i-1]:
            count+=1
        else:
            count=1
        if count>=noOf:
            print("Yes")
            return
    print("No")
for _ in range(int(input())):
    noOf=int(input())
    array=list(map(int,input().split()))
    temp=array[:]
    temp.extend(array)
    count=1
    valid(count,temp,noOf)