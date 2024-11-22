class Student: 
    def getdata(self): 
        self.sid=int(input("Enter sid:")) 
        self.sname=input("Enter sname:") 
        self.saddress=input("Enter saddress:")

    def display(self): 
        print("Student id is:",self.sid) 
        print("Student name is:",self.sname) 
        print("Student address is:",self.saddress) 
s1=Student() 
s1.getdata() 
s1.display()
