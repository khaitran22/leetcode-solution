def maxProfit(prices):
    if len(prices) == 1:
        return 0

    buy, sell = prices[0], prices[0]
    max_profit = sell - buy
    for i in range(1, len(prices)):
        if prices[i] >= sell:
            buy = sell
            sell = prices[i]
            max_profit += (sell - buy)
        else:
            # max_profit += (sell - buy)
            buy = prices[i]
            sell = buy
    return max(0, max_profit)


prices = [1, 4, 7, 8, 6, 4]
print(maxProfit(prices))
