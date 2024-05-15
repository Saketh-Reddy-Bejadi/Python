# https://www.codechef.com/START134D/problems/PRISON

# n,m=map(int,input().split())
# res=[]
# for i in range(n):
#     row=list(map(int,input().split()))
#     if 0 in row:
#         pre=aft=0
#         for j in range(m):
#             if j<row.index(0):
#                 pre+=1
#             elif j>row.index(0):
#                 aft+=1
      
#         res.append(min(pre,aft))
# print(max(res))

for _ in range(int(input())):
    n,m=map(int,input().split())
    res=[]
    for i in range(n):
        row=list(map(int,input().split()))
        if 0 in row:
            pre=aft=0
            for j in range(m):
                if j<row.index(0):
                    pre+=1
                elif j>row.index(0):
                    aft+=1
          
            res.append(min(pre,aft))
    print(max(res))
