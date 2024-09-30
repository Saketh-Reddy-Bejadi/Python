def valid(s):
    arr=s.split(' ')
    for i in range(len(arr)):
        arr[i]=arr[i][0].upper()+arr[i][1:]
    return ' '.join(arr)

print(valid("i love programming"))