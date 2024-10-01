def valid(n):
    if (len(str(n))<3):
        return False
    s=str(n)+str(n*2)+str(n*3)
    print(s)
    for i in range(len(s)):
        if not(str(i+1) in s):
            return False
    return True

print(valid(853))