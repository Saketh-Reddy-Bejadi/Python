def minimumBoxes(apple,capacity):
    w=sum(apple)
    c=0
    capacity.sort(reverse=True)
    for e in capacity:
        if w<=0:break
        w-=e
        c+=1
    return c

print(minimumBoxes([1,3,2],[4,3,1,5,2]))