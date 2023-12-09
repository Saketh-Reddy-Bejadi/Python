import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
def distance(x1, y1, x2, y2):
    dis = math.ceil(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return math.ceil(3.14 * (dis**2))
actual=distance(x1,y1,x2,y2)
occupied=distance(x1,y1,x3,y3)

if (actual==occupied) :
    print(-1)
elif (x1==y1 or x2 ==y2 or x3==y1):
    print(-1)
elif(actual<occupied) :
    diff_land=occupied-actual
    remain_lan=math.ceil(math.sqrt(diff_land))**2
    money=(remain_lan-diff_land)*20
    print("Krishna",money)
else :
    diff_land=actual-occupied
    money=(diff_land)*20
    print("Shiva",money)
    
