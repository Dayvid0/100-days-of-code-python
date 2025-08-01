for row in range(3):
   for col in range(3):
    print("*", end="")
print()  

list1 = ["A", "B"]
list2 = [1, 2]
for letter in list1:
  for number in list2:
    print(f"{letter}{number}")

for i in range(1, 4):
  for j in range(1, 4):
    print(f"{i}x{j}={i*j}", end = " ")
  print()      