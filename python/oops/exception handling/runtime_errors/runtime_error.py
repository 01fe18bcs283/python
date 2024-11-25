# a=10 print(A) #NameError
# a=int(input("Enter a number:")) #Enter a number:abc
#ValueError: invalid literal for int() with base 10: 'abc' 

# print(a) 
print(10+"abc") #TypeError: unsupported operand type(s) for +: 'int' and 'str' 
print(10/0) #ZeroDivisionError: division by zero