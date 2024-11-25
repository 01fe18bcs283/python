class Parent: 
    def property(self): 
        print("Cash+Gold+Lands") 
    def car(self): 
        print("Alto car") 
        
class Child(Parent): 
    def car(self): 
        super().car() 
        print("Benz car")


c=Child() 
c.property() 
c.car()

