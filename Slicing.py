#####SLICING###
quote= "I love python"
print(quote[2:6])  #love
print(quote[7:]) #python ( till the end)
print(quote[-1: 4])

###Skipping values##
print(quote[0:6:2]) #skipping 2 values until 6 characters
print(quote[::3]) #skipping 3 values until the end

##Reversing##
print(quote[::-1]) #reverse the string