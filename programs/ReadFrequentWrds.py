file=input("Enter the file name:")
f=open(file)
str1=f.read().strip()
str2=str1.split()
dict1={}
k=dict1.keys()
for n in str2:
    if n in k:
        dict[n]+=1
    else:
        dict1[n]+=1
max1=max(dict1.values())
print(f"Below word(s) repeated {max1} times")
for key,value in dict1.items():
    if value==max1:
        print(key)
        

        
