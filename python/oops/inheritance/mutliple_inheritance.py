class A: 
    def f1(self): 
        print("F1 function of class A") 
class B: 
    def f2(self):
        print("F2 function of class B") 
class C(A,B): 
    def f3(self): 

        print("F3 function of class C") 
        
c=C() 
c.f1() 
c.f2() 
c.f3()


class X: 
    def f1(self): 
        print("F1 function of class x") 
class Y: 
    def f1(self): 
        print("F1 function of class y") 
class Z(X,Y): 
    def f3(self): 
        Y.f1(self) 
        print("F3 function of class z") 
        
a=Z() 
a.f1() 
a.f3()