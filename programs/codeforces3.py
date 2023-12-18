def count_steps_to_sort(s,n):
    steps = 0
    s_list = list(s)

    for i in range(len(s_list) - 1):
        for j in range(0, len(s_list) - i - 1):
            if s_list[j] > s_list[j + 1]:
                s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
                steps += 1
    
    if steps==n:
        print(-1)
    else:
        print(steps)

t=int(input())
for _ in range(t):
    n=int(input())
    input_string = input()
    steps_needed = count_steps_to_sort(input_string,n)
