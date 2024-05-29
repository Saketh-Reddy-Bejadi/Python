def geometry(s):
    xaxis1=xaxis2=0
    yaxis1=yaxis2=0
    if s[0]=='1':
        xaxis1=-10
    if s[1]=='1':
        xaxis2=10
    if s[2]=='1':
        yaxis1=10
    if s[3]=='1':
        yaxis2=-10
    x=xaxis1-xaxis2+1
    y=yaxis1-yaxis2+1
    return x*y
for _ in range(int(input())):
    string=input()
    print(geometry(string))