def valid(pattern,s):
    d={}
    s=s.split(' ')
    if len(pattern) != len(s):
        return False
    for i in range(len(pattern)):
        if pattern[i] in d:
            if d[pattern[i]]!=s[i]:
                return False
        else:
            if s[i] in d.values():
                return False
            d[pattern[i]]=s[i]
    return True


print(valid("abaa","dog cat cat dog"))