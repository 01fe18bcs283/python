class Test: 
    x=10 
    _y=20 #protected 
    __Z=30 #private 
    def __init__(self): 
        print("within the class") 
        print(self.x) 
        print(self._y) 
        # print(self.__z) 
t=Test() 
print("outside of the class") 
print(t.x) 
print(t._y)
# print(t.__z)--> error



class Parent: 
    a=10 #public 
    _b=20#protected 
    __c=30 #private 
class Child(Parent): 
    print(Parent.a) 
    print(Parent._b) 
    #print(Parent.__c) Error 

child=Child()

class Car: 
    def __init__(self): 
        self.__updatesoftware() 
    def __updatesoftware(self): #private method 
        print("Updating software") 

c=Car() 
#c.__updatesoftware()




class Car: 
    __name="" 
    __maxspeed=0
    def __init__(self): 
        self.__name="thar" 
        self.__maxspeed=100 
        print(self.__name) 
        print(self.__maxspeed) 
    def drive(self): 
        self.__maxspeed=200 #maxspeed will change
        print("Driving") 
        print(self.__name) 
        print(self.__maxspeed) 

c=Car() 
c.__maxspeed=300 #maxspeed will not change 
c.drive()