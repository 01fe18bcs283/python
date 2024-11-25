try: 
    #print(10/0) 
    print("try block") 
except: 
    print("except block") 
    
finally: 
    print("finally block")




# example 2

import os 
try: 
    #print(10/0) 
    print("try block") 
    #os._exit(0) 
    
except: 
    print("Except block") 
    os._exit(0) 
    
finally: 
    print("finally block")