class Person:
  def __init__(self, fname, lname,age):
    self.firstname = fname
    self.lastname = lname
    self.fullage = age
  def printname(self):
    print(self.firstname, self.lastname, self.fullage)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe",30)
x.printname()
