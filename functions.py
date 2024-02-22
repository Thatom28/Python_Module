# why we need functions :
# 1. to avoid repetition and duplication (not DRY
#functions are a way to pack your logic together)


#declaration/ definition
def sum(a, b):  #a nad b are parameters or arguments
  return a + b #function body
  #calling the function
#we have abstracted the logic(because we do not need to know what the implimentation is about)
print("the sum is ", sum(1, 2))


#DEFAULT VALUES
def driving_test(age, car ="Toyota tazz"):
  if age >=18:
    return f"You are eligible for driving. You will be tested with {car} "  #if there is no return it will return none
  else:
    return "Try again after few years😶"

print(driving_test(40))  #will be tested with default
print(driving_test(25, "Gr corolla"))

#TYPES OF ARGUMENTS
#positional argument
#named arguments

