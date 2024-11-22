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



class Salary(Employee): 
    def getsal(self): 
        self.basic=int(input("Enter basic salary:")) 
    def calculate(self): 
        self.DA=self.basic*0.06 
        self.HRA=self.basic*0.4 
        self.Gross=self.basic+self.DA+self.HRA 
    def displaysal(self): 
        print("Basic is:",self.basic) 
        print("DA is:",self.DA) 
        print("HRA is:",self.HRA) 
        print("Gross is:",self.Gross)


s=Salary()
s.getbranchdata() 
s.getempdata() 
s.getsal() 
s.calculate() 
s.displaybranchdata() 
s.displayempdata() 
s.displaysal()