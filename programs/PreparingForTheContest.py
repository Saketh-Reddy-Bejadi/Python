def swap_elements(n, array):
    low, high = 0, n
    while low < high:
        array[low], array[high] = array[high], array[low]
        low += 1
        high -= 1

t = int(input())
for _ in range(t):
    size1, size2 = map(int, input().split())
    array_values = [i + 1 for i in range(size1)]
    swap_elements(size1 - size2 - 1, array_values)
    print(*array_values)
