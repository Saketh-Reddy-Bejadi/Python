def busyStudent(startTime,endTime,queryTime):
    c=0
    for i in range(len(startTime)):
        if startTime[i]<=queryTime<=endTime[i]:
            c+=1
    return c

print(busyStudent([1,2,3],[3,2,7],4))