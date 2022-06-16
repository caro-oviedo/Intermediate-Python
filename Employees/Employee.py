class Employee():
  def __init__(self, frname, lname, salary):
    self.idnum: int
    self.frname = frname
    self.lname =lname
    self._salary = salary
    self.benefits = 1000


  def getSalary(self):
    return self._salary


#Employees dict
class Employees():
  def __init__(self):
    self.empDict = {}
    self.index = 101


  def addEmployee(self, emp):
    emp.idnum = self.index
    self.index += 1
    self.empDict.update({emp.idnum: emp})


  def listEmployees(self): 
    dict = self.empDict
    for key in dict:
      empl = dict[key]
      print(empl.frname, empl.lname, empl.getSalary())


class TempEmployee(Employee):
  def __init__(self, frname, lname, idnum):
    super().__init__(frname, lname, idnum)
    self.benefits = 0

class Intern(TempEmployee):
  def __init__(self, frname, lname, sal):
    super().__init__(frname, lname, sal)
    self.setSalary(sal)


  def setSalary(self, val):
    if val > 500:
      self._salary = 500
    else:
      self._salary = val

class Speaker():
  def inviteTalk(self):
    pass

  def giveTalk(self):
    pass

class PublicEmployee(Employee, Speaker):
  def __init___ (self, frname, lname, salary):
    super().__init__(frname,lname,salary)
