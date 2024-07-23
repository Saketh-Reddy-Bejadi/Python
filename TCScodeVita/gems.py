def maximize_gems(n, dishes):
    pairs = [list(map(int, dish.split(":"))) for dish in dishes]

    pairs.sort(key=lambda x: x[0])

    groups = []
    gems_max_id = gems_min_id = 0

    for pair in pairs:
        if not groups or pair[0] == groups[-1][-1][0] + 1:
            groups[-1].append(pair)
        else:
            groups.append([pair])

    for group in groups:
        gems_max_id += max(group, key=lambda x: x[0])[1]
        gems_min_id += min(group, key=lambda x: x[0])[1]

    print(max(gems_max_id, gems_min_id))


n = int(input())
dishes = input().split()
maximize_gems(n, dishes)
