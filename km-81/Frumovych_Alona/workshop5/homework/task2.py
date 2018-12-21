# Які продукти купляли усі покупці?
from task1 import *
n = {}
for key in result:
    s = []
    n[key] = {}
    b = 0
    for date in result[key]:
        s.append(set(result[key][date].keys()))
    for i in range(len(s)-1):
        if s[i] in s[i+1:] or s[i] == s[len(s)-1]:
            s.pop(i)
    n[key] = s
print(n)