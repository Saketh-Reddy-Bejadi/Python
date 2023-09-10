def anagram(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True

arr1 = input("Enter a string:")
arr2 = input("Enter another string:")

ans = anagram(arr1, arr2)
print(ans)
