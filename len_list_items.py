n = int(input("N = "))
list = []

for item in range(n):
    item = input()
    list.append(item)
print(list)

avr = 0
for item in list:
    avr += len(item)
avr = avr / n
print(f"The average of the lenghs of the items in the list is {avr}")