try: 
    a = int(input("Enter Num1:")) 
    b = int(input("Enter Num2:")) 
    print("result is:", a / b) 

except ZeroDivisionError as msg: 
    print(msg) 

except ValueError as msg: 
    print(msg)

# multiple exceptions

try: 
    a = int(input("Enter Num1:")) 
    b = int(input("Enter Num2:")) 
    print("result is:", a / b) 

except(ZeroDivisionError,ValueError)as msg: 
    print(msg)


# super class "exception"
# this default block should always be last.

try: 
    a = int(input("Enter Num1:")) 
    b = int(input("Enter Num2:")) 
    print("result is:", a / b) 
    
except Exception as msg: 
    print(msg)