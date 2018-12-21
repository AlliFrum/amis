# Створити dataset та працювати з ним
def convert_to_dict(lst):
    if len(lst[0]) == 2:
        return {
            "quantity": lst[0][0],
            "price": lst[0][1]
        }
    dct = {}
    for l in lst:
        key = l[0]
        if key not in dct:
            dct[key] = []
        dct[key].append(l[1:])
    for key in dct:
        dct[key] = convert_to_dict(dct[key])
    return dct
with open('orders.csv', encoding='utf-8') as f:
    f.readline()
    data = [[w.strip() for w in line.split(',')] for line in f]
    result = convert_to_dict(data)
print(result)