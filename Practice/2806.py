def valid(purchaseAmount):
    if 5<=purchaseAmount<10:
        return 100-10
    return 100-round(purchaseAmount/10)*10


print(valid(25))