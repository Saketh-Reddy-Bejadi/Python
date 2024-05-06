candies=[2,3,5,1,3]
extraCandies = 3
m=max(candies)
for i in range(len(candies)):
    candies[i]+=extraCandies
    if candies[i]>=m:
        candies[i]=True
    else:
        candies[i]=False
print(candies)