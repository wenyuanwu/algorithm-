def buy_and_sell(arr):
	min_price_so_far, max_profit = float("inf"), 0 
	for price in arr:
		current_profit = price - min_price_so_far
		max_profit = max(max_profit, current_profit)
		min_price_so_far = min(price, min_price_so_far) 
	return max_profit	

arr = [20,30,0,50,90]
arr2 = [50,30,0,10]
print(buy_and_sell(arr2))