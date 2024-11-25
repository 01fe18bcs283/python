from abc import ABC,abstractmethod 

class Vehicle(ABC): 
    @abstractmethod 
    def wheels(self): 
        pass 
    def engine(self): 
        print("Bs6 engine") 

    @abstractmethod 
    def color(self): 
        pass

class Car(Vehicle): 
    def wheels(self): 
        print("Car:4 wheels") 
    def color(self): 
        print("Car:color is red") 
    
class Bike(Vehicle): 
    def wheels(self): 
        print("Bike:2 wheels") 
    def color(self): 
        print("Bike:color is black") 
        
c=Car() 
c.wheels() 
c.engine() 
c.color() 
b=Bike() 
b.wheels() 
b.engine() 
b.color()