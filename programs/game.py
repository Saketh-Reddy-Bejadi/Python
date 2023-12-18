# def count_occurrences(s, target):
#     count = 0
#     for c in s:
#         if c == target:
#             count += 1
#     return count

# test_cases = int(input())
    
# for _ in range(test_cases):
#     q = input().strip()
#     p = count_occurrences(q, '0')
#     z = count_occurrences(q, '1')
#     ans = []

#     for i in range(len(q)):
#         if q[i] == '0' and z < 1:
#             break
#         if q[i] == '1' and p < 1:
#             break
#         if q[i] == '0' and z > 0:
#             ans.append('1')
#             z -= 1
#         elif q[i] == '1' and p > 0:
#             ans.append('0')
#             p -= 1

#     print(abs(len(q) - len(ans)))


def count_occurrences(string, target_char):
    count = 0
    for char in string:
        if char == target_char:
            count += 1
    return count


test_cases = int(input())

for _ in range(test_cases):
    input_string = input().strip()
    count_zeroes = count_occurrences(input_string, '0')
    count_ones = count_occurrences(input_string, '1')
    result = []

    for i in range(len(input_string)):
        if input_string[i] == '0' and count_ones < 1:
            break
        if input_string[i] == '1' and count_zeroes < 1:
            break
        if input_string[i] == '0' and count_ones > 0:
            result.append('1')
            count_ones -= 1
        elif input_string[i] == '1' and count_zeroes > 0:
            result.append('0')
            count_zeroes -= 1

    print(abs(len(input_string) - len(result)))

