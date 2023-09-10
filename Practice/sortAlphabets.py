def sort_alphabets(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string

text = input("Enter a string: ")
sorted_text = sort_alphabets(text)
print("Sorted alphabets:", sorted_text)
