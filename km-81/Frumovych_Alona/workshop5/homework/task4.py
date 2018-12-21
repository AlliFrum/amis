# Скільки грошей витрачає кожний покупець на покупки? (графік)
from task1 import *
import plotly
import plotly.graph_objs as go
p = {}
for key in result:
    p[key] = {}
    b = 0
    for date in result[key]:
        for prod in result[key][date]:
            b += (float(result[key][date][prod]['quantity'])*float(result[key][date][prod]['price']))
    p[key] = b
print(p)

diagram = go.Scatter(x=list(p.keys()), y=list(p.values()))
fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='amount_of_money.html')