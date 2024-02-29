from math import pi
from datetime import datetime

salary= 420000
#--Numeric separators
salary2 =4_20_000
print(salary)  #when progam runs it will print 420000

print(f"Dhara's salary id R{salary2}")
print(f"Dhara's salary id R{salary2:,}") #what to separate with

print(f"the PI value is: {pi: .2f}")    #how many number to rond it off to
print(f"the PI value is: {round(pi)}")  #Whole number

name ="lilitha"

#default: will print spaces
print(f"{name:<20}:")  #moves to ten left
print(f"{name:>20}:") #move the name to the right by 20 spaces
print(f"{name:^20}:")  #for centering

#Padding
print(f"{name:#<20}:") #prints # after the name
print(f"{name:&>20}:") #prints & 20 times ( before the name)
print(f"{name:(^20}:")

caleb = 0.9250
print(f"the the test results out and Caleb got {caleb:.2%}")

now = datetime.now()
print(f"the current date is : {now:%d/%m/%Y}")
print(f"the current date is : {now:%d-%B-%Y}") #full month name
print(f"the current date is : {now:%d-%b-%Y}") #abbriviated month name
