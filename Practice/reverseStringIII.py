def valid(s):
    s=s.split(' ')
    r=''
    for w in s:
        r+=w[::-1]+" "
    return r.strip()
    
    
print(valid("Let's take LeetCode contest"))