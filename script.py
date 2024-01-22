# Carly's Clippers

# Initial lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculating the total price
total_price = 0

# Adding each price to the total price
for price in prices:
  total_price += price

# Calculating the average price
average_price = total_price / len(prices) # Prices' length
print("Avegare Haircut Price: " + str(average_price))

# Creating a new list with list comprehension with 5 dollar less each price
new_prices = [price - 5 for price in prices]

# Calculating the revenues
total_revenue = 0

for i in range(len(hairstyles)): # creating a range object in the length of hairstyles
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))

# Average daily revenue (total / 7)
average_daily_revenue = total_revenue / 7

# Haircuts under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)
