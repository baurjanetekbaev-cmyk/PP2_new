class myclass:
    x=5

#Now we can use the class named MyClass to create objects:
p1=myclass()
print(p1.x)

#You can delete objects by using the del keyword:
#del p1

#You can create multiple objects from the same class:
p1=myclass()
p2=myclass()
p3=myclass()
print(p1.x)
print(p2.x)

#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass


#Create a class without __init__()
class Person:
  pass
p1 = Person()
p1.name = "Tobias"
p1.age = 25
print(p1.name)
print(p1.age)

#You can also set default values for parameters in the __init__() method:
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)

#Use self to access class properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil", 25)
p1.greet()

#Access multiple properties using self:
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

#Create a class with properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)

#Create a method in a class:
class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()

#Create a method with parameters:
class Calculator:
  def add(self, a, b):
    return a + b
  def multiply(self, a, b):
    return a * b
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

#Without the __str__() method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1)







