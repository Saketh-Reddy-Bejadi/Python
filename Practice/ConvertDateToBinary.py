def convertDateToBinary(date):
    nums=date.split('-')
    res=[]
    for i in nums:
        res.append(bin(int(i))[2:])
    return '-'.join(res)


print(convertDateToBinary(date = "2080-02-29"))