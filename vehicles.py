class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Car(Vehicle):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

class Bus(Vehicle):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

class Van(Vehicle):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

cars = [Car('Audi', 'A6', 10000), Car('Mercedes', 'C220', 15000), Car('Opel', 'Astra', 4000)]

buses = {Bus('Mecedes Benz', 'Citaro', 450000), Bus('Volvo', '9700', 750000)}

vans = [Van('Chevrolet', 'Express Work Van', 41800), Van('Ford', 'Transit Connect Trend', 30000), Van('Volkswagen', 'ID. Buzz Cargo', 32000)]

while True:
    type = str(input("What are you looking for(plural)? ")).lower()
    if type.endswith('s'):
        break;

if type == 'cars':
    for car in cars:
        print(f'{car.brand} {car.model} {car.price}$')
elif type == 'buses':
    for bus in buses:
        print(f'{bus.brand} {bus.model} {bus.price}$')
elif type == 'vans':
    for van in vans:
        print(f'{van.brand} {van.model} {van.price}$')
else:
    print("We dont have any vehicles of that sort right now.")

