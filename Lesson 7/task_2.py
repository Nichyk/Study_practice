# Compute the total price of the stock where the total price is the sum of the price of an item
# multiplied by the quantity of this exact item.
# Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_items = {}
for key in stock.keys():
    if key in prices:
        total_items[key] = stock[key] * prices[key]
total_price = sum(value for value in total_items.values())
print(total_price)
