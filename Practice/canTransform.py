def can_transform(s1, s2):
    if len(s1)!=len(s2):
        return False
    s={}    
    for i,j in zip(s1,s2):
        f=(ord(j)-ord(i))%26
        b=(ord(i)-ord(j))%26        
        if(i in s):
            if(s[i]!=f and s[i]!=b):return False
        else:s[i]=f
    return True

s1="abab"
s2="fdfz"
print(can_transform(s1,s2))
