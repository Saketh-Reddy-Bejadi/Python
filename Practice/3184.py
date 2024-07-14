def valid(hours):
    n,c=len(hours),0
    for i in range(n):
        for j in range(i+1,n):
            if (hours[i]+hours[j])%24==0:
                c+=1
    return c
    
hours = [12,12,30,24,24]
print(valid(hours))