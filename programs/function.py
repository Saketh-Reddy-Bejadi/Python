def add(li,e):
    last=len(li)
    li[last:]=[e]
    
li=[1,2,3,4,5]
e=int(input("Enter a element"))
add(li,e)
add(li,e)
add(li,e)

print(li)