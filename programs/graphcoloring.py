colors=['red','blue','green','yellow','black']
states=['andhra','karnataka','tamilnadu','kerala']
neighbors={}
neighbors['andhra']=['karnataka','tamilnadu']
neighbors['karnataka']=['andhra','tamilnadu','kerala']
neighbors['tamilnadu']=['andhra','karnataka','kerala']
neighbors['kerala']=['karnataka','tamilnadu']

r={}
def valid(s,c):
    for n in neighbors.get(s):
        cn=r.get(n)
        if c==cn:
            return False
    return True
def getcolor(s):
    for c in colors:
        if valid(s,c):
            return c
for s in states:
    r[s]=getcolor(s)
    
print(r)