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


# pull numbers from a string

s = ' I love 2 go t0 the store 7 times a week'

nums = [x for x in s if x.isnumeric()]
print(''.join(nums))

# get index of a list item

names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print(idx)

# delete item in list using comprehension

letters = [x for x in 'ABCDEF']
new_list = [a for a in letters if a != 'C']
print(new_list)

### if-else in a comprehension

nums = [2, 4, 6, 8, 9, 10, 11]
filtered = [x ** 2 if x % 2 == 0 else x ** 3 for x in nums]  # if even then square, else cube it
print(filtered)
