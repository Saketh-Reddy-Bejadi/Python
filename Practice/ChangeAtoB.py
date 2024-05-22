# for _ in range(int(input())):
#     a,b,k=map(int,input().split())
#     c=0
#     while(True):
#         if b%k==0 and k>=a:
#             c+=1
#             b//=k
#         elif b%k==0:
#             c+=b-a
#             break
#         else:
#             c+=b%k
#             b-=b%k
#     print(c)
for _ in range(int(input())):
    a, b, k = map(int,input().split())
    c = 0
    while True:
        if b % k == 0 and b // k >= a:
            c += 1
            b //= k
        elif b % k == 0:
            c += b - a
            break
        else:
            c += b % k
            b -= b % k
    print(c)