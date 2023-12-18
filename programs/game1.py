def count_occurrences(input_str, target_char):
    count = 0
    for char in input_str:
        if char == target_char:
            count += 1
    return count

def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        input_str = input().strip()
        count_zeroes = count_occurrences(input_str, '0')
        count_ones = count_occurrences(input_str, '1')
        result = []

        for i in range(len(input_str)):
            if input_str[i] == '0' and count_ones < 1:
                break
            if input_str[i] == '1' and count_zeroes < 1:
                break
            if input_str[i] == '0' and count_ones > 0:
                result.append('1')
                count_ones -= 1
            elif input_str[i] == '1' and count_zeroes > 0:
                result.append('0')
                count_zeroes -= 1

        print(abs(len(input_str) - len(result)))

if __name__ == "__main__":
    main()
