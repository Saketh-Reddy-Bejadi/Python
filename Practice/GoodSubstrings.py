def valid(S):
    ans=0
    zeroCount=0
    for i in range(len(S)):
        if int(S[i])==0:
            zeroCount+=1
        if int(S[i])%2!=0:
            ans+=(i+1)
            ans-=zeroCount
    return ans
S="1234"
print(valid(S))