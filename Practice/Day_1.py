#------------- TASK1 :faherits to celcius----------------------------

# temp_faherits = float(input("Enter the temperature in Fahrenheit: "))

# temp_celcus = (5/9)*(temp_faherits-32)
# print(f"the temperature i s{temp_celcus} °C")

# ---------TASK2 : fIND THE AGE OF THE PERSON------------------------

# import datetime
# year = int(input("Enter your year of birth: "))
# current_year = datetime.datetime.now().year
# print(f"you are {current_year - year} years old")

#--------TASK3 : PROGRESS LEVEL-------------------------

# number = int(input("Enter progress amount: "))
# num =int(number/10)
# num_empty = int(10 - num)
# print("[" + "=" * num +  " " * num_empty +"]")
# print(f"[{'=' * num} {' '* num_empty}]")


#----------SLICING EXAMPLES---------------
# quote = "I love programming, ut it needs a lot of passion"

# #when you want the word "love" only
# print(quote[2:7])

# #When we want to skip 2 letter everytime
# print (quote[::2])

# #when you want to reverse the string
# print(quote[::-1])

# print(quote[-1:4:1])

#----------CONDITIONAL STATEMENTS-----------------

# marks = [45,23,12,34,65,43,56,87,56,34,65,24,65,87,99]
# for mark in marks:
#   if(mark >=80):
#    print(str(mark) + " distiction")
    
#   elif(mark >=50):
#     print(str(mark) + " above average")
  
#   elif(mark >=30):
#     print(str(mark) + " below average")
  
# else:
#   print(str(mark) + " fail")

#----------ICE CREAM SHOP-----------------------

#TASK 1

# cus_flavour= input("whats your flavour: ")
# ice_cream_flavours = ["chocolate", "vanilla", "strawberry"]

# if cus_flavour in ice_cream_flavours:
#   print("we have it😍")
# else:
#   print("sorry out of stock😢")

# TASK 2: REFINING THE ABOVE SOLUTION

cus_flavour= input("whats your flavour: ")
ice_cream_flavours = ["chocolate", "vanilla", "strawberry"]

print("we have it😍" if cus_flavour in ice_cream_flavours else "sorry out of stock😢" )



