n = int(input("How many items in the list? "))
list = []
print("Input elements:")
for i in range(n):
    item = input()
    list.append(item)

if len(list) != len(set(list)):
    print("There are equal elements.")
else:
    print("There aren't equal elements.")