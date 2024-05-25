for _ in range(int(input())):
    noOfEle = int(input())
    array = list(map(int, input().split()))
    array.sort()
    temp = 0
    i = 1
    while i < noOfEle:
        if array[i] % array[0]:
            if temp:
                if array[i] % array[temp]:
                    break
            else:
                temp = i
        i += 1
    print("Yes" if i >= noOfEle else "No")