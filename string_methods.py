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