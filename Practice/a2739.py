def fun(mainTank,additionalTank):
    ans = 0
    while True:
        if mainTank>=5 and additionalTank>=1:
            mainTank = mainTank-4
            additionalTank -=1 
            ans += 50 
        else:
            ans += mainTank*10
            return ans
mainTank=5
additionalTank=10
print(fun(mainTank,additionalTank))

