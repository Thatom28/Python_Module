from math import pi
c

salary= 420000
salary2 =4_20_000
print(salary)  #when progam runs it will print 420000

print(f"Dhara's salary id R{salary2}")
print(f"Dhara's salary id R{salary2:,}") #what to separate with

print(f"the PI value is: {pi: 2f}")    #how many number to rond it off to
print(f"the PI value is: {round(pi)}")

name ="lilitha"

print(f"{name:<20}:")   
print(f"{name:>20}:") #move the name to the left by 20 spaces
print(f"{name:^20}:")  #for centering

print(f"{name:#<20}:")   
print(f"{name:&>20}:") #mprints 20 ( before the name)
print(f"{name:(^20}:")

caleb = 0.9250
print(f"the the test results out and Caleb got {caleb:.2%}")

now = datetime.now()
print(f"the current date is : {now:%d-%m-%Y}")