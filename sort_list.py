n = int(input("Number of items in list? "))
list = []

print("Input elements: ")
for i in range(n):
    item = int(input());
    list.append(item)
print(list)
list.sort()
print(list)