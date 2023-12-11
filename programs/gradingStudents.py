import math

n=int(input())
for _ in range(0,n):
    grades=int(input())


for i in range(0,n):
    a=math.ceil(grade/5)
    b=a*5
    
    if b-grade<3:
        grade=b
print(grades)