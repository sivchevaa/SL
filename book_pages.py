K = int(input("K = "))

digits = 1
N = 0

while True:
    pages_in_block = 9 * (10 ** (digits - 1))
    digits_in_block = pages_in_block * digits
    if K > digits_in_block:
        K -= digits_in_block
        N += pages_in_block
        digits += 1
    else:
        N += K // digits
        break

print(N)