def buy_sell_stocks(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price,price)
        profit = price - min_price
        max_profit = max(profit,max_profit)
    return max_profit
print(buy_sell_stocks([7,1,5,3,6,4]))    