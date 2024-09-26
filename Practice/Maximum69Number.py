def valid(num):
    res=set()
    num=str(num)
    for i in range(len(num)):
        if num[i]=='6':
            res.add(int(num[:i]+'9'+num[i+1:]))
        else:
            res.add(int(num[:i]+'6'+num[i+1:]))
    num=int(num)
    return max(res) if max(res)>num else num
print(valid(9996))