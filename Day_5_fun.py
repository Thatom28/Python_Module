# #importing cool methods
# import Day_5_cool

# #nb the whole cool file is running
# print(Day_5_cool.to_upper_case("Alex"))


#--------other ways to import
#------specify the method that you want
from Day_5_cool import to_upper_case as to_upper

print(to_upper("Gemma"))  #use the name in your aliase as your function name

#----Have an alies for the methods with the same name
import Day_5_cool as cool

print(cool.to_upper_case("Alex"))
print(to_lower_case("James"))
#ctrl + space to get the list of methods
from math import sqrt