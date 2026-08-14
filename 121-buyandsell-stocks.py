# 121. Best Time to Buy and Sell Stock
prices = [7,6,4,3,1]
buy = prices[0]
profit = 0 
for i in prices : 
    if i < buy : 
        buy = i 
    else : 
        current_profit = i - buy
        if current_profit > profit : 
            profit = current_profit 

print(profit)
