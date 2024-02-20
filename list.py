#List are muttable, meaning they can change
marks = [98, 75, 40, 45, 80, 60]
avarage = [100, 90, 80, 70, 60, 50]

# print(marks)
# print(marks.pop(3))  # removes the last element in the list  #mutate
# lenth = len(marks)
# print(lenth)
# print(marks[0: len(marks) -3])  #slicing the integers cutting the last 3 integers, does not change the original list
# print(marks[0:-3]) #same as above
# print(marks)

#removing an item on the list (removing 40)
# marks.remove(40)    #changes teh array
# print(marks)

#adding an item to the list (adds to the end)
eng = 88
marks.append(eng)        #Muatates
print(marks)

#inserting to a speciifc index
marks.insert(2,eng)  # (the index, the value to insert)
print(marks)

print( marks * 2) #prints the list twice

#duplicating list
print(marks * 3)
# adding two list together (combining them)
print(marks + avarage) #98, 75, 40, 45, 80, 60, 100, 90, 80, 70, 60, 50