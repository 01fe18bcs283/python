from modules.calculate import add
from modules.calculate import sub
from modules.calculate import product
from modules.calculate import div
from modules.calculate import even
from modules.calculate import prime
from modules.calculate import amstrong
from modules.calculate import reverse
from modules.calculate import factorial
from modules.calculate import factors
from modules.calculate import count_factor

x,y=20,10
print(add(x,y))
print(sub(x,y))
print(product(x,y))
print(div(x,y))
print(even(x))
print(prime(x))
print(amstrong(x))
l=[10,20,30,40,50]
print("reversed list:",reverse(l))
print("factorial of {x} is :",factorial(x))
print("factors of {x} is :",factors(x))
print("number of factors of {x} is :",count_factor(x))

