for _ in range(int(input())):
    n = int(input())
    s = input()
    uni = set(s)
    r = sorted(list(uni))
    r1 = r[::-1]
    t = {}
    for i in range(len(r)):
        t[r[i]] = r1[i]
    ans=""
    for c in s:
        ans+=t[c]
    print(ans)
