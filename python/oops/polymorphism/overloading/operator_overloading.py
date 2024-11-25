# We can use the same operator for multiple purposes, which is nothing but operator overloading.


class Book: 
    def __init__(self,pages): 
        self.pages=pages 

b1=Book(10) 
b2=Book(20) 
# print(b1+b2) #TypeError:


# Magic Methods
# For every operator Magic Methods are available. To overload any operator we have to override that Method in our class.


# example 1

class Book_info: 
    def __init__(self,pages): 
        self.pages=pages 
    def __add__(self, other): 
        return self.pages+other.pages 
    def __mul__(self, other): 
        return self.pages*other.pages 
    
c1=Book_info(10) 
c2=Book_info(20) 
print(c1+c2) 
print(c1*c2)


# example 2

class Employee: 
    def __init__(self, name, salary): 
        self.name = name 
        self.salary = salary 
    def __mul__(self, other): 
        return self.salary * other.days 
    
class TimeSheet: 
    def __init__(self, name, days): 
        self.name = name 
        self.days = days 
        
e = Employee('Durga', 500) 
t = TimeSheet('Durga', 25) 
print('This Month Salary:', e * t)