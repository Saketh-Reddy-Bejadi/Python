for _  in range(int(input())):
    N=int(input())
    if N == 1:
        print("ALICE")
    elif N % 2 == 1:
        print("BOB")
    else:
        print("ALICE")

