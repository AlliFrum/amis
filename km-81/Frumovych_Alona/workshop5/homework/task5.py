# Який найпопулярніший товар?
from task1 import *
list_prods = []
for key in result:
    for date in result[key]:
        for key_ in result[key][date].keys():
            string = str(key_)
            list_prods.append(string)
count = {}
for prod in set(list_prods):
    a = 0
    a = list_prods.count(prod)
    count[prod] = a
val = count.values()
mx = max(val)
for key in count:
    if mx == count[key]:
        print('The most popular product: ', key)
