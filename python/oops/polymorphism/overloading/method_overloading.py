# If 2 methods having same name but different type of arguments then those methods are said to be overloaded methods.
# Python will always consider only last method.

class Test: 
    def m1(self): 
        print("no arg method") 
        
    def m1(self,a): 
        print("one arg method") 

    def m1(self,a,b): 
        print("two arg method")
        
t=Test() 
#t.m1()
#  #t.m1(10) 
t.m1(10,20)




