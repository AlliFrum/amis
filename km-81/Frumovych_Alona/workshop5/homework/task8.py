# Якого товару, скільки покупців купляє? (графік)
from task1 import *
import plotly
import plotly.graph_objs as go
lst = {}
for key in result:
    quantity = 0
    for date in result[key]:
        for prod in result[key][date]:
            quantity += float(result[key][date][prod]['quantity'])
    lst[key] = quantity
print(lst)
diagram = go.Scatter(x = list(lst.keys()), y = list(lst.values()))
fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='quantity.html')