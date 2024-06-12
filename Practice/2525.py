length = 1
width = 1
height = 10000
mass = 1
b = False

p = length * width * height

if length >= 10000 or width >= 10000 or height >= 10000 or p >= 1000000000:
    b = True

h = mass >= 100

if b and h:
    print("Both")
elif not b and not h:
    print("Neither")
elif b:
    print("Bulky")
else:
    print("Heavy")