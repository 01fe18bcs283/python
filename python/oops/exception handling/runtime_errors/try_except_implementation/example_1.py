# Syntax:
#      try:
#           Statements
#      except:
#           Statements
#  In general inside the try block we include risky statements and inside except block we include handling statements.
#  If no exception occurs inside the try block then try block statements will execute and except block will ignore.
#  If any exception occurs inside the try block then try block will ignore and except block will execute.

try:
    a = int(input("Enter Num1:")) 
    b = int(input("Enter Num2:")) 
    print("result is:", a / b) 
except : 
    print("something went wrong")