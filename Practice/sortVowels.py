def valid(s):
    s=list(s)
    vowels='aeiouAEIOU'
    vowelsList=[c for c in s if c in vowels]
    vowelsList.sort()
    indx=0
    for i in range(len(s)):
        if s[i] in vowels:
            s[i]=vowelsList[indx]
            indx+=1
    return ''.join(s)


print(valid("lYmpH"))