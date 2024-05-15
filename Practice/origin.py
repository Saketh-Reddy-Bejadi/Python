# n=int(input())
# s=r=0
# for i in range(1,n+1):
#     if i<10:
#         r+=i
#     else:
#         while(i>10):
#             d=i%10
#             s+=d
#             i/=10
#         r+=s
# print(r)







def func(n):
    s = 45
    f = n // 9
    re = n % 9
    return f * s + (re * (re + 1)) // 2
for i in range(int(input())):
    num = int(input())
    print(func(num))
