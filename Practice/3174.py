s = "cb34"
sList=list(s)
i=0
while(True):
    if sList[i] in '0123456789':
        sList.remove(s[0])
        sList.remove(s[i])
    i+=1    
print(sList)::