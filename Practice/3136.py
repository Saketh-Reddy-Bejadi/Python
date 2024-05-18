word = "234Adas"
def valid(word):
    v="aeiouAEIOU"
    c="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    hv=hc=False
    if len(word)<3:
        return False
    for i in word:
        if (not i.isalnum()):
            return False
        if i in v:
            hv=True
        if i in c:
            hc=True
    return hv and hc