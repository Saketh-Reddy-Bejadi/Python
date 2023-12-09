def maximize_gems(n, dishes):
    # Split the input into pairs of id and rating
    pairs = [list(map(int, dish.split(":"))) for dish in dishes]

    # Sort the pairs based on the id
    pairs.sort(key=lambda x: x[0])

    # Initialize variables to keep track of groups and gems
    groups = []
    gems_max_id = gems_min_id = 0

    for pair in pairs:
        if not groups or pair[0] == groups[-1][-1][0] + 1:
            groups[-1].append(pair)
        else:
            groups.append([pair])

    # Calculate gems for maximum id and minimum id separately
    for group in groups:
        gems_max_id += max(group, key=lambda x: x[0])[1]
        gems_min_id += min(group, key=lambda x: x[0])[1]

    # Print the maximum gems
    print(max(gems_max_id, gems_min_id))


# Example usage
n = int(input())
dishes = input().split()
maximize_gems(n, dishes)
