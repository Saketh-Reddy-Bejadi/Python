def totalFine(date,car,fine):
    a=date%2==0
    print(a)
    r=0
    for i in range(len(car)):
        if a:
            if car[i]%2!=0:
                r+=fine[i]
        else:
            if car[i]%2==0:
                r+=fine[i]
    return r

date=12
car=[2375,7682,2325,2352]
fine=[250,500,350,200]
print(totalFine(date,car,fine))