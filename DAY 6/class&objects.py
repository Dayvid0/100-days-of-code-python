# Student class with an object
class Student:
 pass
student1 = Student
#Class called animal no method and create objects 
class Animals:
 pass
animal1 = Animals()
animal2 = Animals()
animal3 = Animals()
#Create a class Book that takes title and author during object creation.
class Book:
 def __init__(self, title,author):
  self.title = title
  self.author = author
# 🔹 3. __str__() Method
# Add a __str__ method to your Book class so that printing an object shows the title and author.
 def __str__(self):
   return (f"{self.title} by {self.author}")
book1 = Book("Things Fall Apart", "Chinua Achebe")
print(book1.title)
print(book1.author)
print(book1)

#Create a class Phone that takes brand, model, and price. Initialize them in the constructor.  
class Phone:
 def __init__ (self, brand, model, price):
  self.brand = brand
  self.model = model
  self.price = price
phone1 = Phone("Samsung", "Galaxy A52", 1200000)
print(phone1.brand, phone1.model, phone1.price)

# Create a Movie class with name, year, and rating, and override __str__() to print it nicely.
class Movie:
 def __init__(self, name, year, rating):
  self.name = name
  self.year = year
  self.rating = rating
 def __str__(self):
   return (f"{self.name} released in {self.year} has a rating of {self.rating}")
 def __str__(self):
        return f"{self.name} ({self.year}) - Rating: {self.rating}/10"

Movie1 = Movie("Lord of Wars", "2005", "4.3/5")
print(Movie1)
movie2 = Movie("The Matrix", 1999, 8.7)
print(movie2)
#Create a class Dog with a method bark() that prints something.
class Dog:
  def bark(self):
    print("woof! woof!")
dog1 = Dog()
dog1.bark()

#Create a class Calculator with methods: add, subtract, multiply, and divide.
class Calculator:
  def add(self, a, b):
    result = a + b
    return f'{a} + {b} = {result}'
  def subtract(self, a, b):
    return a - b
  def multiply(self, a, b):
    return a * b
  def divide(self, a, b ):
    result = a/b
    return f"{a} / {b} = {result}"
calc = Calculator()
# Example usage
print("Addition:", calc.add(10, 5))        
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))     







