def remove_anagrams(words):
    result = []
    for word in words:
        if not result or sorted(word) != sorted(result[-1]):
            result.append(word)
    return result

words1 = list(map(input().split()))
print(remove_anagrams(words1))
