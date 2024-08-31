def valid(s,k):
    n=len(s)
    res=''
    for i in range(0,n,k):
        subString=s[i:i+k]
        hashSum=0
        for char in subString:
            hashSum+=ord(char)-ord('a')
        res+=chr((hashSum%26)+ord('a'))
    return res
print(valid("abcd",2))