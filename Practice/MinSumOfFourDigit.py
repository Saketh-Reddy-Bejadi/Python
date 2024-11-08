def valid(num):
    arr=[]
    while(num>0):
        arr.append(num%10)
        num=num//10
    arr.sort()
    num1=num2=0
    for i in range(len(arr)):
        if(i%2==0):
            num1*=10
            num1+=arr[i]
        else:
            num2*=10
            num2+=arr[i]
    return (num1+num2); 

num = 2932 
print(valid(num))
