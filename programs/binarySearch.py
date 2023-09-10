def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target element not found

# Example usage:
numbers = list(map(int,input("Enter list of elements:").split()))
target_number = int(input("Enter element for search:"))

result = binary_search(numbers, target_number)
if result != -1:
    print(f"Element {target_number} found at index {result}")
else:
    print(f"Element {target_number} not found in the list.")
