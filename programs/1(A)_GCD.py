n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
i=1
while(i<=n1 and i<=n2):
    if (n1 % i == 0 and n2 % i == 0):
        gcd = i
    i+=1

print(f"GCD of {n1} and {n2} is {gcd}")

