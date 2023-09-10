def count_vowels(string):
    vowels = "aeiou"
    count = 0

    for char in string.lower():
        if char in vowels:
            count += 1

    return count

text = input("Enter a string: ")
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
