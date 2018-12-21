# Якого товару було куплено найменше?
from task1 import *
from task5 import val, count
mn = min(val)
print("The least popular products:")
for key in count:
    if mn == count[key]:
        print(key, end = ' ')