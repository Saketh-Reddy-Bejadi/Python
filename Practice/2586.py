words = ["vo","j","i","s","i"]
left = 0
right = 3
c=0
v='aeiou'
for w in words[left:right+1]:
    if w[0] in v and w[-1] in v:
        c+=1
print(c)