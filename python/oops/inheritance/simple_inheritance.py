class Branch: 
    def getbranchdata(self):
        self.bcode=int(input("Enter branch code:"))
        self.bname=input("Enter branch name:") 
        self.baddress=input("Enter branch address:")

    def displaybranchdata(self): 
        print("Branch code is:",self.bcode) 
        print("Branch name is:",self.bname) 
        print("Branch address is:",self.baddress) 
class Employee(Branch): 
    def getempdata(self): 
        self.eid=int(input("Ente eid:")) 
        self.ename=input("Enter ename:") 
        self.eaddress=input("Enter eaddress:") 
            
    def displayempdata(self): 
        print("Empid is:",self.eid) 
        print("Ename is:",self.ename) 
        print("Eaddress is:",self.eaddress)

s=Employee()
s.getbranchdata()
s.getempdata()
s.displaybranchdata()
s.displayempdata()
