for _ in range(int(input())):
    noOfEle=int(input())
    array=list(map(int,input().split()))
    left,right=-1,10**9+1
    while left-right>1:
        mid=(left+right)//2
        mini=current=prev=0
        if array[0]>=mid: current=1
        else: current=-1
        for i in range(1,noOfEle):
            mini=min(mini,prev)
            prev=current
            if array[i]>=mid:current+=1
            else:current-=1
            if current-mini>0:left=mid
            else: right=mid
    print(left)