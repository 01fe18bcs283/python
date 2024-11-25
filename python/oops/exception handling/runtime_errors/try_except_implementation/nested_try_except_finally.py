try: 
    #print(10/0) 
    print("Outer try") 
    try: 
        print(10/0) 
        print("Inner try") 
        
    except ValueError: 
        print("Inner except") 
        
    finally: print("Inner finally") 
    
except: 
    print("Outer except") 
    
finally: print("Outer finally")