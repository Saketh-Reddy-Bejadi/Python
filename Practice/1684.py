def valid(allowed,words):
    count=0
    for word in words:
        if all(a in allowed for a in word):
            count+=1
    return count


allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(valid(allowed,words))