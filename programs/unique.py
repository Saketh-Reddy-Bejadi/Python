arr = list(map(int, input().split()))
unique_list = []

for num in arr:
    if arr.count(num) == 1:
        unique_list.append(num)

print(unique_list)
