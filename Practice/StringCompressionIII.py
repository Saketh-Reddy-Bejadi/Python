word = "aaaaaaaaaaaaaabb"
# freq={}
# for i in word:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# # print(freq)
# s=""
# for i,v in freq.items():
#     if v>9:
#         while(v>9):
#             s+=i
#             s+=str(v-9)
#             v-=9
#         s+=i
#         s+=str(9)
#         s=s[::-1]
#     else:
#         s+=str(v)
#         s+=i  
# print(s)
string=""
count=1
for i in range(len(word)):
    if i+1<len(word) and word[i]==word[i+1]:
        count+=1
        if count==9:
            string+=str(count)+word[i]
            count=0
    else:
        if count>0:
            string+=str(count)+word[i]
            count=0
        count=1
print(string)