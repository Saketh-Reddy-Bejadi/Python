def valid(s1,s2):
    s=s1+" "+s2
    words=s.split()
    wordsCount={}
    for word in words:
        if word not in wordsCount:
            wordsCount[word]=1
        else:
            wordsCount[word]+=1
    uncommonWords=[]
    for i in wordsCount.keys():
        if wordsCount[i]==1:
            uncommonWords.append(i)
    return uncommonWords

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(valid(s1, s2))