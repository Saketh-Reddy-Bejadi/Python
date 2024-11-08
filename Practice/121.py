def maxProfit(p):
    if not p:
        return 0
    
    minPrice = p[0]
    maxProfit = 0
    
    for i in p:
        minPrice = min(minPrice, i)
        maxProfit = max(maxProfit, i - minPrice)
    
    return maxProfit
        
prices = [2,4,1]
print(maxProfit(prices))