def ball(n,k):
    posi,dir =0, 1

    for _ in range(k):
        if dir == 1:
            if posi == n - 1:
                dir = -1
            posi += dir
        else:
            if posi == 0:
                dir = 1
            posi += dir

    return posi
n=5
k=6
print(ball(n,k))