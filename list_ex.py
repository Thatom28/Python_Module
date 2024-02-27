scarmbled_message = "world the save to time no is there"
#get the string to a list (you can split by any character) (, \n : ;)
splitted_message = scarmbled_message.split(" ")
print(splitted_message)
# reverse the words using slicing
reversed_message = splitted_message[::-1]
print(reversed_message)

#use the join function
corrected_message = " ".join(reversed_message)
print(corrected_message)
print(" ".join(reversed_message))

#------limited split
limited_split = "apple,banana,cherry,dragonfruit".split(",", 2)  #splitting only th e first 2
print(limited_split)


