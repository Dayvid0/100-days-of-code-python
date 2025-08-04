# #CREATE A PYTHON CLASS
# class myclass:
#   x = 5
# print(myclass)  

# # CREATE AN OBJECT P1 IN THE CREATED CLASS (myclass)
# p1 = myclass()
# print(p1.x)

#_init_() MEthod
class  person:
 def __init__(self, name, age):
   self.name = name
   self.age = age

p1 =person('John', 36)
print(p1.name)
print(p1.age)

p2 = person("Okullo David", 22)
print(f"{p2.name} is  {p2.age} years old!")
print(p1.name + " " + str(p1.age))

p3 = person("Abdul", 25)
print(f"{p3.name} is {p3.age} years old!")
print(p3.name + " " + str(p3.age))

#car class
class car:
  def __init__(self, brand, mileage):
    self.brand = brand
    self.mileage = mileage

car1 = car("Mercedes", 200)
car1.mileage = 400
del car1.brand
print(f"{car1.mileage}")
print(car1.mileage)