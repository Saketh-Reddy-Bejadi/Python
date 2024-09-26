def valid(boxTypes,truckSize):
    for i in range(len(boxTypes)):
        for j in range(0, len(boxTypes) - i - 1):
            if boxTypes[j][1] < boxTypes[j + 1][1]:
                boxTypes[j], boxTypes[j + 1] = boxTypes[j + 1], boxTypes[j]
    boxesInTruck=0
    for box in boxTypes:
        if box[0]<=truckSize:
            boxesInTruck+=box[0]*box[1]
            truckSize-=box[0]
        else:
            while(truckSize>0):
                truckSize-=1
                boxesInTruck+=1*box[1]
    return boxesInTruck
            
    
print(valid([[5,10],[2,5],[4,7],[3,9]],10))