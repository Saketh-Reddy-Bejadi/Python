def valid(n):
    count=0
    for i in range(3,n+1):
        if i%3==0 or i%5==0 or i%7==0:
            count+=i
    return count

print(valid(9))