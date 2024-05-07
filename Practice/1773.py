items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
c=0
v=1 if ruleKey=='type' else (2 if ruleKey=='color' else 3)
for i in range(len(items)):
    if items[i][v-1]==ruleValue :
        c+=1  
print(c)