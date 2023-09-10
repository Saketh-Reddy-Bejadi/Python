def patter1(n):
    for row in range (1,n+1):
        for col in range(1,row+1):
            print("*",end=" ")
        print("")

patter1(4)



def sum(n1,n2) :
    sum=0
    for i in range(n1,n2+1) :
        sum+=i
    return sum

print(sum(1,100))
