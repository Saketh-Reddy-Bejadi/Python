def can_make_zero(arr, n):
    operations_needed = [0] * n

    # Calculate the operations needed for each element
    for i in range(1, n - 1):
        operations_needed[i] = max(0, arr[i] - arr[i - 1])

    # Perform the operations
    for i in range(1, n - 1):
        if arr[i] < operations_needed[i]:
            return "NO"
        arr[i] -= operations_needed[i]
        arr[i + 1] -= operations_needed[i]
        operations_needed[i + 1] += operations_needed[i] * 2

    # Check if all elements become zero
    return "YES" if all(x == 0 for x in arr) else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_make_zero(arr, n))
