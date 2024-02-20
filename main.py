#name = "Lee"
#print(name)
#print("Hello, my name is " + name)

#name1 = input(" what is my name: ")
#print(name1)

# Task 1 --. faherits to celcius

  #temp_fahre =float (input ("Enter temperature in faheinheit: ")) 
  
  #temp_celc = float (temp_fahre - 32) * 5/9
  
  #print( str(temp_celc) + "°C") 

#Simplyfy task 1
  #print(f"The temperature in celcius is {temp_celc}°C")

#Task 2 find the age of the person
#year = input("Enter the year you were born: ")
#age = 2024 - int(year)
#print(f"You are {age} years old")
#print(f"You are {2024 - int(year)} years old")

#Task 3 -- area of the circle
#import math
#radius = input("Enter the radius of the circle: ")
#print(f"The area of the circle is {math.pi * float(radius) ** 2}")

# Task 3
#value = int (input("Enter number: "))
#n = value/ 10
#empty = 10 - n
#print("=" * int(n) + " " * int(empty) + " " + str(value) + "%")

##Yolanda  solution
num = input("Enter a number ")
num1 = int(num) // 10
spaces = 10 - num1
eq = "=" * num1
sp = " " * spaces
print(f"{spaces} spaces left")
#print("["+str(eq)+ sp +"] "  + num + "%")


