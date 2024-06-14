x1,y1,x2,y2,x3,y3=map(int,input().split())
px1,py1=x2-x1,y2-y1
px2,py2=x3-x1,y3-y1
cPro=px1*py2-px2*py1
if cPro>0:
    print("LEFT")
elif cPro<0:
    print("RIGHT")
else:
    print("TOUCH")