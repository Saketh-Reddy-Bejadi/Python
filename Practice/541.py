def valid(s,k):
    s = list(s)
    i=0
    while(i<len(s)):
        t=s[i:k][::-1]
        s=s[:i]+t+s[k:]
        i+=k*2
        k+=i
    return s
        :
s="krmyfshbspcgtesxnnljhfursyissjnsocgdhgfxubewllxzqhpasguvlrxtkgatzfybprfmmfithphckksnvjkcvnsqgsgosfxc"
k=20
print(valid(s,k))