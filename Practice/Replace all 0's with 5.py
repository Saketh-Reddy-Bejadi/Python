def convertFive(n):
    if '0' not in str(n):return n
    n=str(n)
    # while('0' in n):n=n.replace('0','5')
    for i in range(len(n)):
        if n[i]=='0':n=n[:i]+'5'+n[i+1:]
    return int(n)
print(convertFive(1004))