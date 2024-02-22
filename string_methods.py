#FORMATTING A TEXT
msg = "Hi, all"
print(msg.upper())  #to convert to uppercase
print(msg.lower()) #to covert to lower cases
print(msg.title()) #to convert to title case, capitalize first letter of a word
print(msg.capitalize()) #to capitalize the first letter of the string 

msg1="       dreams are something you see in sleep"
print(msg1.strip()) # removes spaces
msg2 ="-----dreams are something you see---"
print(msg2.strip("-")) # removes the - from the string
print(msg2.lstrip("-")) # removes the - from the left side
print(msg2.rstrip("-")) # removes the - from the right side
print(msg2.find("are")) #returns index of "are" returns the index of the first match

print(msg2.strip("-*")) # removes the - and * from the string

print(msg2.replace("are" , "is")) #replaces are with is, if you return the string it will return the original string
msg3 ="dreams are something you see"
# strings are case sensitive
print(msg3.count("are")) #= 1
print(msg3.count("Are")) #= 0
print(msg3.startswith("d")) #= True
print(msg3.endswith("D")) #= False

print(len(msg3)) #to get the legth of the string

print(msg3.islower())  #True return a boolean to check if the text is in lower case
###integers
badge_num = "3453"
print(badge_num.isdigit()) #= True