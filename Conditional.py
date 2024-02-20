person1 =input("please enter your name: ")
height1 = input("provide your heigt in cm: ")

person2 =input("please enter your name: ")
height2 = input("provide your heigt in cm: ")

if (height1 > height2):
  print(f"{person1} is taller ")
else:
  print(f"{person2} is taller ")  

#Problem is with the lexico order because it uses the strings to compare the heights
#SOLUTION parse  the stings to integers

person1 =input("please enter your name: ")
height1 = int(input("provide your heigt in cm: "))

person2 =input("please enter your name: ")
height2 = int(input("provide your heigt in cm: "))

if (height1 > height2):
  print(f"{person1} is taller ")
elif(height1 < height2):
  print(f"{person2} is taller ")  
else: 
  print(f"{person1} and {person2} are the same height")