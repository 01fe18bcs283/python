import time 
class Test: 
    def __init__(self): 
        print("Constructor execution") 
    def __del__(self): 
        print("Destructor execution") 

t=Test() 
time.sleep(5) 
print("End of the program")