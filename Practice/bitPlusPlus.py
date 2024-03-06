n=int(input())
num=0
for _ in range(n):
    string=input()
    if "++" in string:
        num+=1
    if "--" in string:
        num-=1
print(num)