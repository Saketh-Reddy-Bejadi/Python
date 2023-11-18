def avg(x):
    sum=0.000
    for i in x:
        sum=(sum+i)
    return sum/len(x)
nums = list(map(int, input().split()))

print(avg(nums))