numbers=list(map(int,input("Enter elemetns:").split()))
element=int(input("Enter element to search:"))
for i in range (len(numbers)-1):
    if numbers[i]==element:
        print(f"{element} found at index {i}")
        break
else:
    print(f"{element} not found in the list")