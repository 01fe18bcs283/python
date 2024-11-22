import modules.calculate as calculate
x,y=20,10
print(calculate.add(x,y))
print(calculate.sub(x,y))
print(calculate.product(x,y))
print(calculate.div(x,y))
print(calculate.even(x))
print(calculate.prime(x))
print(calculate.amstrong(x))
l=[10,20,30,40,50]
print("reversed list:",calculate.reverse(l))
print("factorial of {x} is :",calculate.factorial(x))
print("factors of {x} is :",calculate.factors(x))
print("number of factors of {x} is :",calculate.count_factor(x))