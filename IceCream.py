flavour =input("enter your flavour: ")

#Task 1
#stock1 ="vanilla"
#stock2 = "lime"
#stock3 ="chocolate"

#if (flavour == stock1 or flavour == stock2 or flavour == stock3):  #or is written "or" in python and "and"
 # print("yes, we do have it")
#else:
#   print("No, we ran out of stock")

#task 2
#shop_stock = "vanilla, lime, chocolate"
#if (flavour in shop_stock):        #to check if the input string is in the shop_stock string, you can                             check even separate wods in the string i.e. " lla, li" it will return true.
# print("yes, we do have it")
#else:
#  print("No, we ran out of stock")

#Refactor -> Code quality up
#Binary operator ( comapres two inputs) ("==" '!=' "<" ">" "<=" ">=")') includes the arithmetic operators
#Unary (takes one thing)(boolean)
#bitwise operators(& , ~ ,  )
#Refactoring the code

#Task 3
shop_stock = ["vanilla, lime, chocolate"]
# print("yes, we have it") if flavour in shop_stock else print("No, we ran out of stock")
# or
result = "yes, we have it" if flavour in shop_stock else "No, we ran out of stock"
print(result)

print("yes we do have it" if flavour in shop_stock else "no, we do not have it")