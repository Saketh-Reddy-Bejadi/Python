def valid(paragraph,banned):
    words=''
    for char in paragraph:
        if char.isalpha() or char.isspace():
            words+=char.lower()
        else:
            words+=' '
    paragraph=words
    print(paragraph)
    words = paragraph.split()
    count={}
    for word in words:
        if word not in banned:
            if word in count:
                count[word]+=1
            else:
                count[word]=1
    c=0
    res=''
    for i in count.keys():
        if count[i]>c:
            c=count[i]
            res=i
    return res
    



paragraph ="a, a, a, a, b,b,b,c, c"
banned = ["a"]
print(valid(paragraph,banned))