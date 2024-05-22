for _ in range(int(input())):
    l=int(input())
    s=input()
    s=list(s)
# #     while(len(set(s))>1):
# #         r=[]
# #         for i in range(l):
# #             if s[i]=='1':
# #                 r.append(i)
# #             elif s[i]!='1' and len(r)>0:
# #                 if min(r)!=max(r):
# #                     m1=max(r)+1
# #                     m2=min(r)
# #                     m3=m1-m2
# #                     s[m2:m1]=["0"]*m3
# #                 else:
# #                     s[max(r)]='0'
# #                 c+=1
# #                 r=[]
# #     print(c)
    count0 = 0
    count1 = 0
    for i in range(l):
        if s[i] == '0':
            if i == 0 or s[i-1] != '0':
                count0 += 1
        else:
            if i == 0 or s[i-1] != '1':
                count1 += 1
    print(min(count1,count0))