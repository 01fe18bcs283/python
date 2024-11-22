class Test: 
    def __init__(self): 
        self.a=10 
        self.b=20 
    def m1(self): 
        print("within the class") 
        print(self.a) 
        print(self.b) 
t=Test() 
t.m1() 
print("outside of the class") 
print(t.a) 
print(t.b)