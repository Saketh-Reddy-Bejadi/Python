s=input()
while('AB' in s or 'CD' in s):
    for i in range(len(s)):
        if i<len(s):
            if s[i]=='A' and s[i+1]=='B':
                s=s[:i]+s[i+2:]
                break
            elif s[i]=='C' and s[i+1]=='D':
                s=s[:i]+s[i+2:]
                break
        else:
            i=0
print(len(s))
