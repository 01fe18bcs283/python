class Parent: 
    def f1(self): 
        print("Parent class method") 
class Child1(Parent): 
            def f2(self): 
                print("Child1 class method") 
class Child2(Parent): 
    def f3(self): 
        print("Child2 class method") 


c1=Child1() 
c2=Child2() 
c1.f1() 
c1.f2() 
c2.f1() 
c2.f3()