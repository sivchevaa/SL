car1 = {
    "brand": input("Brand: "),
    "model": input("Model: "),
    "hp": int(input("Horsepower: "))
}

car2 = {
    "brand": input("Brand: "),
    "model": input("Model: "),
    "hp": int(input("Horsepower: "))
}

if car1["hp"] > car2["hp"]:
    print(f"{car1["brand"]} {car1["model"]} is faster")
elif car1["hp"] < car2["hp"]:
    print(f"{car2["brand"]} {car2["model"]} is faster")
else:
    print("Both have the same speed.")