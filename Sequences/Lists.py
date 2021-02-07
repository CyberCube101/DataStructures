''' Lists grow and shrink as required..'''

b = [i ** 2 for i in range(10) if i > 4]

print(b)

x = [5, 3, 8, 6]
y = x.copy()
# insert 7 in the 1st place
x.insert(1, 7)
print(x)

# POP REMOVES THE LAST ITEM OFF LIST AND RETURNS ITEM

print(x.pop(), x)

# reverse and sort are in-place methods. sorted(x) is not an inplace method

x.sort()
print(x)
x.sort(reverse=True)
print(x)
print(sorted(y))
print(y)

## list comprehension


