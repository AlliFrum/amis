# Який найдорожчий товар?
from task1 import *
prices = {}
for key in result:
    for date in result[key]:
        for key_ in result[key][date].keys():
            price = float(result[key][date][key_]['price'])
            prices[key_] = price
max_price = max(prices.values())
for key in prices:
    if max_price == prices[key]:
        print(key)