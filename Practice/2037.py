seats = [3,1,5]
students = [2,7,4]
seats.sort()
students.sort()
MinSteps=0
for i in range(len(students)):
    MinSteps+=abs(students[i]-seats[i])
print(MinSteps)