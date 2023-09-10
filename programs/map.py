arr=[1,2,3,4,5]
def Array(x):
    return x+1
newArray=list(map(Array,arr))
print(newArray)