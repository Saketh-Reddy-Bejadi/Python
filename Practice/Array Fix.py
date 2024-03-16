def can_make_sorted(arr):
    sorted_arr = sorted(arr)
    n = len(arr)
    i = 0
    j = 0
    while i < n and j < n:
        if arr[i] >= 10:
            digit_arr = [int(d) for d in str(arr[i])]
            if sorted_arr[j:j+len(digit_arr)] == digit_arr:
                j += len(digit_arr)
            else:
                return "NO"
            i += 1
        else:
            if arr[i] == sorted_arr[j]:
                i += 1
                j += 1
            else:
                return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_make_sorted(arr))