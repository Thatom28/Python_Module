#TASK 1

# message = "    🚨🔍📱🔑secret_code✌️"
# code="SECRET_CODE✌️"

# #after te key print out the rest of the text
# key = message.find("🔑")
# output = message[key+ 1::].upper()

# if(output == code):
#   print("You are a hacker")
# else:
#   print("try again")

#TASK 2

# message = "    🚨🔍📱secret_code✌️"
# code="SECRET_CODE✌️"

# #If the key is not present
# key = message.find("🔑")

# if (key < 0):
#   print("No key present")
# else:
#   output = message[key+ 1::].upper()
  
#   if(output == code):
#     print("You are a hacker")
#   else:
#     print("try again")

# TASK 3

message = "    🚨🔍📱🔑***secret_code✌️)))"
code="SECRET_CODE✌️"

#after te key print out the rest of the text
key = message.find("🔑")
output = message[key+ 1::].upper()
# remove_star = output.strip("*")
# remove_bracket = remove_star.strip(")")
remove_junk = output.strip("*").strip(")")  #REFINED
print(remove_junk)

#Dot chaining continues when you are still in string
replaced_code = message.replace("secret", "🙈")
print(replaced_code)
reversed_code = message[::-1]    #you have created a new string that contains reverse string
print(reversed_code)
