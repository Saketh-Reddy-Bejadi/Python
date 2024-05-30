def verify(s):
    temp = list(s)  
    if sorted(temp) == list(s):
        print("Yes")
    else:
        print("No")

for _ in range(int(input())):
    lenOfS = int(input())
    String = input()
    verify(String)