def maxProfit(prices):
    if len(prices) == 1:
        return 0
    
    buy = prices[0]
    sell = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
            sell = buy
        else:
            if prices[i] > sell:
                sell = prices[i]
        max_profit = max(max_profit, sell - buy)
    return max(0, max_profit)

# prices = [2,4,1]
prices = [9,8,7,6,8,4,1]


print(maxProfit(prices))