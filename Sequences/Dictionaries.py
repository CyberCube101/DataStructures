'''Dictionaries are key/value pairs

They are unordered too'''

x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
y = dict(pork=25.3, beef=33.8, chicken=22.7)
z = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])  # list of tuples

print(x)
print(y)
print(z)

x['shrimp'] = 38.2
print(x)

#### keys, values

print(x.keys())
print(y.values())
print(x.items())
print('beef' in y.keys())

### iteration

for k, v in y.items():
    print(k, v)

for key in y:
    print(key, y[key])
