class Parent: 
    def f1(self):
        print("Parent class method") 
class Child1(Parent): 
    def f2(self): 
        print("Child1 clas method") 
class Child2(Parent): 
    def f3(self): 
        print("child2 class method") 

c1=Child1() 
c2=Child2() 
print(isinstance(c1,Child1)) #true 
print(isinstance(c2,Child2)) #true 
print(isinstance(c1,Child2)) #false 
print(isinstance(c2,Child1)) #false 
print(isinstance(c1,Parent))# true 
print(isinstance(c2,Parent))# true 
print(issubclass(Child1,Parent)) #true 
print(issubclass(Child2,Parent)) #true 
print(issubclass(Child1,Child2)) #false 
print(issubclass(Child2,Child1)) #false