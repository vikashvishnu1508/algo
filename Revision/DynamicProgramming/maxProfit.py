def maxProfit(prices):
    min_price = prices[0]
    max_profit = -float('inf')
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, (prices[i] - min_price))
    return max_profit




prices = [10, 7, 5, 8, 11, 9]
print(maxProfit(prices))