# Small, Smaller, Smallest

for _ in range(int(input())):
    lenOfStr=int(input())
    binaryString=input()
    onesCount = binaryString.count('1')    
    if onesCount==0:
        print(lenOfStr)
    elif onesCount%2==1:
        print(1)
    else:
        print(0)