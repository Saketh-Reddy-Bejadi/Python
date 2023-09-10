n=int(input("enter no of elements:"))
L=[]
for i in range(0,n):
    value=int(input(f"enter the element {i+1}:"))
    L.append(value)
    
print("Given Elements are:",L)

def maximum(L):
    _max=L[0]
    for i in L:
        if _max<i:
            _max=i
            
         
    print("Largest element is:",_max)
    
maximum(L)
