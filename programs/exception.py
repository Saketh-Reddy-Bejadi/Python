a=input("Enter a number:")
try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")
except Exception as a:
    print(a)
print("Program ended")   