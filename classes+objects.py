# Challenge: Classes and Objects

'''
Instructions-
1. Create a class called Person
2. Add an __init__ method that takes name and age as parameters
3. Add a method called greet that prints "Hello, my name is " followed by the name
4. Create an object p1 of the class with name and age
5. Call the greet method on p1
'''

# Create a class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} old!")

# Create an object
p1 = Person("Ray", 42)

# Call the greet method
p1.greet()