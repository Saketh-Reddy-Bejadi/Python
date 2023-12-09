def find(integers, k):
    integers.sort()
    moves = 0
    max_count = 1
    length = len(integers)
    start = 0
    current = 0
    end = length - 1
    result = 1
    
    while moves < length:
        if integers[current] < k:
            moves += 1
            max_count += 1
            result = max(result, max_count)
            k -= integers[current]
            start += 1
            
            if current + 1 < length and integers[current + 1] < k:
                current += 1
            else:
                current = end
        else:
            moves += 1
            max_count -= 1
            result = max(result, max_count)
            k += integers[current]
            current = start
            end -= 1
    
    return result

def main():
    input_str = input()
    k = int(input())
    integers = list(map(int, input_str.split()))

    result = find(integers, k)
    print(result)

if __name__ == "__main__":
    main()
