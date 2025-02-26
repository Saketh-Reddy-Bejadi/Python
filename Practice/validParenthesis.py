def valid(s):
    stack=[]
    n=len(s)
    if(n&1==1): return False
    for i in range(n):
        if(s[i]=='{' or s[i]=='(' or s[i]=='['):
            stack.insert(0,s[i])
        else:
            if(len(stack)==0): return False
            c=stack[0]
            if((c=='{' and s[i]=='}') or (c=='[' and s[i]==']') or (c=='(' and s[i]==')')):
                stack.pop(0)
            else: return False
    return len(stack)==0

s = "[{()}]"
print(valid(s))