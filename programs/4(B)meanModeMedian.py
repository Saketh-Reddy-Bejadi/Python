a= list(map(int,input ("Enter list of elements:").split()))
print ("Mean", sum(a)/ len(a))
a.sort ()
if (len(a)%2 == 1):
    print("Median=",a[len (a)//2])
else:
    print("Media = ",(a[len (a)//2-1] + a [len (a)//2])/2)
dict1={}
for i in a:
    keys = dict1.keys()
    if i in keys:
        dict1[i]+=1
    else:
        dict1[i]=1
max1=max(dict1.values())
mode=[]
for i in dict1:
    if dict1[i]==max1:
        mode.append(i)
print ("Mode", mode)