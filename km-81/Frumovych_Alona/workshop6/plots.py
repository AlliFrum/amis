from exam import *
import plotly
import plotly.graph_objs as go
from plotly import tools
print(incomeDict)
b = a.count('Female')
bar = go.Bar(
    x = list(dct.keys()),
    y = [b]
             )
bar_ = go.Bar(
    x = list(incomeDict.keys()),
    y = list(incomeDict.values())
)
plot = tools.make_subplots(rows = 1, cols = 2)
plot.append_trace(bar, 1, 1)
plot.append_trace(bar_, 1, 2)
plotly.offline.plot(plot, filename = 'plot.html')