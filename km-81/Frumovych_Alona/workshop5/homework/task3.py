# Як змінювалась ціна на яблука? (графік)
from task1 import *
import plotly
import plotly.graph_objs as go
ap = {}
for key in result:
    for date in result[key]:
        ap_ = 0
        if 'apple' in result[key][date].keys():
            ap_ = float(result[key][date]['apple']['price'])
            ap[date] = ap_
print(ap)
diagram = go.Scatter(x=list(ap.keys()), y=list(ap.values()))
fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='apples.html')