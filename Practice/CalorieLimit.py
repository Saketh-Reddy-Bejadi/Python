for _ in range(int(input())):
    noOfSweets,calorieLimit=map(int,input().split())
    sweetsCalorie=list(map(int,input().split()))
    sweetsCount=0
    for n in sweetsCalorie:
        calorieLimit-=n
        if calorieLimit>=0:
            sweetsCount+=1
    print(sweetsCount)