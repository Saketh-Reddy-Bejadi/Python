def destCity(paths):
    d={}
    for i in paths:
        d[i[0]]=i[1]
    for j in paths:
        if j[1] not in d:
            return j[1]
    return ""


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))