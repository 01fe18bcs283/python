# If 2 constructors having same name but different type of arguments then those methods are said to be overloaded constructors.
# python will always consider only last constructor.


class Test: 
    def __init__(self): 
        print("no arg constructor") 
        
    def __init__(self,a): 
        print("one arg constructor") 
        
    def __init__(self,a,b): 
        print("two arg constructor") 
        
#t =Test() 
#t =Test(10) 
t=Test(10,20)



