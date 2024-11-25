# Types of exceptions: 
#     1. Predefined exceptions 
#     2. User defined exceptions 


#  Predefined exceptions also called as built-in exceptions. 
#  The exceptions which are raised automatically by Python virtual machine whenever a particular event occurs are called pre-defined exceptions. 
 
 
#  User defined exceptions are also called as customized exceptions. 
#  Sometimes we have to define and raise exceptions explicitly to indicate that something goes wrong ,such type of exceptions are called User Defined Exceptions or Customized Exceptions 
#  Programmer is responsible to define these exceptions and Python not having any idea about these. 
# Hence we have to raise explicitly based on our requirement by using "raise" keyword.


class Too_oldException(Exception): 
    def __init__(self,arg): 
        self.msg=arg 

class Too_youngException(Exception): 
    def __init__(self,arg): 
        self.msg=arg 
        
try: 
    age = int(input("Enter your age:")) 
    if age > 60: 
        raise Too_oldException("Age should not exceed 60") 
    elif age < 16: 
        raise Too_youngException("Age should not be under 16") 
    
    else: print("You are eligible to take policy") 
    
#except 
# (Too_youngException,Too_oldException,ValueError) as msg: 
except Exception as msg: print(msg)