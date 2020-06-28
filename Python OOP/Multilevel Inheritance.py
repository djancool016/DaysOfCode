class Employee :
    def __init__ (self,idEmp,name,email,phone): 
        self.idEmp = idEmp
        self.name = name
        self.email = email
        self.phone = phone 
        
class Staff(Employee) :     
    def __init__(self,education,*args):  
        super().__init__(*args)
        self.education = education         
        self.umr = 2700000 
         
class Programmer(Staff): 
    def __init__ (self,progLang,*args): 
        salaryRate = 1.40         
        super().__init__(*args)         
        self.progLang = ', '.join(progLang)         
        self.salary = self.umr*salaryRate

    def showinfo(self): 
        print (f'ID : {self.idEmp}\nName : {self.name}\nEmail : {self.email}\nPhone : {self.phone}\nEducation : {self.education}\nPosition : Programmer\nProgramming Language : {self.progLang}\nSalary: {self.salary:.0f}')
         

emp1 = Programmer(('Python','Java','C#'),'S1','G21180094','Dwi Julianto','dwijulianto16@gmail.com','089678690051') 
emp1.showinfo()
 
# Output :
# ID : G21180094
# Name : Dwi Julianto
# Email : dwijulianto16@gmail.com
# Phone : 089678690051
# Education : S1
# Position : Programmer
# Programming Language : Python, Java, C#
# Salary: 3780000
