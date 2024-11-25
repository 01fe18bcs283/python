from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    
    def sleep(self):
        print("This animal is sleeping.")

class Dog(Animal):

    def sound(self):
        print("Bark!")

class Cat(Animal):

    
    def sound(self):
        print("Meow!")

dog = Dog()
dog.sound() 
dog.sleep()  

cat = Cat()
cat.sound()  
cat.sleep() 

# animal = Animal()  ----->  This will raise an error as we cannot instantiate an abstract class
