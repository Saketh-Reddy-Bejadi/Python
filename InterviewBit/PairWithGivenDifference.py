def valid(A,B):
    seen = set()
    for num in A:
        if (num - B) in seen:
            return 1
        seen.add(num)
    return 0

A = [5, 10, 3, 2, 50, 80]
B = 78
print(valid(A,B))