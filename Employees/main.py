from Employee import Employee, Employees, TempEmployee, Intern, PublicEmployee

fred = Employee("Fred", "Silver", 1200)
sam = Employee("Sam", "Snerd", 1300)
tom = TempEmployee("Tom", "Ruiz", 700)
rafael = Intern("Rafael", "Lopez", 800)
mathias = PublicEmployee("Mathias", "Other", 1200)


employessGroup1 = Employees()
employessGroup1.addEmployee(fred)
employessGroup1.addEmployee(sam)
employessGroup1.addEmployee(tom)
employessGroup1.addEmployee(rafael)
employessGroup1.addEmployee(mathias)

print(employessGroup1.empDict.keys())

print(employessGroup1.listEmployees())
