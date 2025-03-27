# Question 1

def factorial(x):
    
    if x == 0 or x == 1:
        print(f"factorial({x}) = 1 (Base Case)")  
        return 1
    
    result = x * factorial(x - 1) 
    print(f"factorial({x}) = {x} * factorial({x - 1}) = {result}")  
    
    return result

n = int(input("Please enter a value to calculate fibonacci: "))
print(f"{n}! = {factorial(n)}")

# Question 2

from math import pi

def factorial(x):

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def sine_x(x_deg, n):

    x = x_deg * pi / 180  
    sinex = 0
    factorialTerm = lambda i: ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)

    for i in range(n + 1):
        sinex += factorialTerm(i)

    return sinex

# Question 3 

totalSum = 0

def recursive_sum(n):
    
    global totalSum
    if n == 0:
        return
    totalSum += n
    recursive_sum(n - 1)

if __name__ == "__main__":
    print("----- 1. factorial(x) -----")
    x = 5
    print(f"{x}! = {factorial(x)}")

    print("\n----- 2. sine_x(x_deg, n) -----")
    x_deg = 30
    n = 5
    print(f"sin({x_deg}) = {sine_x(x_deg, n)}")

    print("\n----- 3. recursive_sum(n) -----")
    n = 10
    totalSum = 0  
    recursive_sum(n)
    print(f"Sum (From 1 to {n}): {totalSum}")
