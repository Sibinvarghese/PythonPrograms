class Employee:
    company_name="Luminar"
    def __init__(self,id,design,sal):
        self.id=id
        self.designation=design
        self.salary=sal

    def printEmp(self):
        print("eid",self.id)
        print("designation",self.designation)
        print("Salary", self.salary)
        print("Employee name", Employee.company_name)

emp=Employee(1001,"sibin",3000)
emp.printEmp() 