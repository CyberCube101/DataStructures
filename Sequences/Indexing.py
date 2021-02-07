''' Python DataStructures

List
Dictionary
Tuples
Strings
Sets
Stacks

'''

x = 'computer'  # start:end+1:step - works on strings, lists and tuples

print(x[1:4])
print(x[1:6:2])  # step 2
print(x[-3:])
print(x[:-2])  # everything except last 2 items

y = [7, 8, 3]
for i, v in enumerate(y):  # returns index and item
    print(i, v)

z = [2, 5, 8, 12]

print(sum(z[-2:]))  # sum last 2 items

### Lets say we want to sort by the second letter in each word using a lambda function

words = ['Kevin', 'Kalvin', 'Korty', 'Kupton']

new_list = sorted(words, key=lambda k: k[2])

print(new_list)



