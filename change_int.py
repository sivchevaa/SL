def swap(a, b):
    temp = a
    a = b
    b = temp
    print("a = ", a)
    print("b = ", b)

a = int(input("Въведете стойност за a: "))
b = int(input("Въведете стойност за b: "))
swap(a,b)