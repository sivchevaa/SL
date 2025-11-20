n = int(input("N = "))
list = []

for item in range(n):
    item = int(input())
    list.append(item)
print(list)

sum = 0
for item in list:
    sum += item ** 2
print(f"The sum is: {sum}")