# Normal is Good (Easy)

for _ in range(int(input())):
    lenOfA=int(input())
    arrA=list(map(int,input().split()))
    arrayCount=0
    Len=1
    for i in range(1,lenOfA+1):
        if i<lenOfA and arrA[i]==arrA[i-1]:
            Len+=1 
        else:
            arrayCount+=(Len*(Len+1)//2)
            Len=1
    print(arrayCount)