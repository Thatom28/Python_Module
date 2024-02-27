#---------STRIING EXERCISES----------------
#-----find the words after 🔑

# message = "    🚨🔍📱🔑secret_code✌️"
# code="SECRET_CODE✌️"

# key_index = message.find("🔑")
# found_code = message[key_index + 1::].upper()
# print(found_code)

#-----if the key is not present
# message = "    🚨🔍📱🔑secret_code✌️"
# code="SECRET_CODE✌️"

# key_index = message.find("🔑")
# print("key not found" if key_index < 0 else  message[key_index + 1::].upper())

#-----if there is junk in the message

# message = "    🚨🔍📱🔑*****secret_code✌️)))))"
# code="SECRET_CODE✌️"

# key_index = message.find("🔑")
# print("key not found" if key_index < 0 else message[key_index+ 1::].strip("*)").upper())

#------LISTS------------
marks = [98, 75, 40, 45, 80, 60]
avarage = [100, 90, 80, 70, 60, 50]

print(marks)
marks.append(67)
marks.insert(4, 67)
print(marks , *marks)

marks_copy = marks.copy()
marks_copy.append(43)
marks.append(99)
print(marks_copy)
print(marks)

marks_copy2 = marks[:4]
print(marks_copy2)