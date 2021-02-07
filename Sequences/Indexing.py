x = 'computer'  # start:end+1:step - works on strings, lists and tuples

print(x[1:4])
print(x[1:6:2])  # step 2
print(x[-3:])
print(x[:-2])  # everything except last 2 items

y = [7, 8, 3]
for i, v in enumerate(y):  # returns index and item
    print(i, v)
