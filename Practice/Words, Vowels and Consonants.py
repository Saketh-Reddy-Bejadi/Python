for _ in range(int(input())):
    s=input()
    vc=cc=sc=0
    v='aeiouAEIUO'
    w=False
    for c in s:
        if c==' ':
            if w:
                sc+=1
                w=False
        elif c.isalpha():
            if not w: w=True
            if c in v: vc+=1
            else: cc+=1

    if w:sc+=1
    print(sc,vc,cc)