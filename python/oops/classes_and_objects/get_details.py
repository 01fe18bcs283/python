class Student: 
    def __init__(self): 
        self.sid=123 
        self.sname="sai" 
        self.saddress="hyderabad" 
    def display(self): 
        print("Student id is:",self.sid) 
        print("Student name is:",self.sname) 
        print("Student address is:",self.saddress) 
s1=Student() 
s2=Student() 
s1.display() 
s2.display()