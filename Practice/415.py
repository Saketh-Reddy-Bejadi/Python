num1 = "11"
num2 = "123"
pNum1=len(num1)-1
pNum2=len(num2)-1
carry=0
result=""
while(pNum1>=0 or pNum2>=0):
    n1=int(num1[pNum1]) if pNum1>=0 else 0
    n2=int(num2[pNum2]) if pNum2>=0 else 0
    cSum=carry+n1+n2
    result+=str(cSum%10)
    carry=cSum//10
    pNum1-=1
    pNum2-=1
if carry:
    result+=str(carry)
print(result[::-1])
