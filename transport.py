n = int(input("Въведете брой километри: "))
time = input("Въведете период от деня (ден/нощ): ")

if time == "ден":
    taxi = 0.70 + n * 0.79
else:
    taxi = 0.70 + n * 0.90

bus = n * 0.09
train = n * 0.06

if n < 20:
    print(taxi)
elif n < 100:
    if bus < taxi:
        print(bus)
    else:
        print(taxi)
else:
    if train < bus and train < taxi:
        print(train)
    elif bus < taxi:
        print(bus)
    else:
        print(taxi)
