set = {'peach', 'chips', 'pizza', 'orange', 'apple', 'banana', 'cherry'}
list = ['apple', 'pizza']

for item in list:
    if item in set:
        set.remove(item)

print(set)