import math
def factorial(n):
    r=1
    for i in range(2,n+1):
        r *= i

    return r

n= int(input("enter the number:"))
print(f"factorial of {n} is {factorial(n)}")

print(f"factorial of {n} is {math.factorial(n)}")