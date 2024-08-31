def valid(num1,num2,num3):
    num1 = str(num1)
    num2 = str(num2)
    num3 = str(num3)
    num1='0'*abs(len(num1)-4)+num1
    num2='0'*abs(len(num2)-4)+num2
    num3='0'*abs(len(num3)-4)+num3
    key=""
    for i in range(4):
        key+=str(min(int(num1[i]),int(num2[i]),int(num3[i])))
    return int(key)
print(valid(1,10,1000))
