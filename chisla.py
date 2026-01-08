class Computation:
    def __init__(self):
        pass
    
    def Factorial(self, n):
        if n < 0:
            return "Factorial not defined for negative numbers"
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    
    def Sum(self, n):
        return (n*(n+1)) / 2
    
    def tableMult(self, n):
        lines = []
        for i in range(1, 11):
            line = f"{i} x {n} = {i * n}"
            lines.append(line)
            print(line)

    def listDiv(self, n):
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors
    
Compute = Computation ()
print(Compute.Factorial(5))
print(Compute.Sum(5))
print(Compute.tableMult(5))
print(Compute.listDiv(5))
