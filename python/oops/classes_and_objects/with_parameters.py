class Student: 
    def __init__(self,x,y,z): 
        self.sid=x 
        self.sname=y 
        self.saddress=z 
    def display(self): 
        print("Student id is:",self.sid) 
        print("Student name is:",self.sname) 
        print("Student address is:",self.saddress) 
s1=Student(101,"sai","hyderabad") 
s2=Student(102,"mohan","sr nagar") 
s1.display() 
s2.display()