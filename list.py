#List are muttable, meaning they can change
marks = [98, 75, 40, 45, 80, 60]
avarage = [100, 90, 80, 70, 60, 50]

# print(marks)
# print(marks.pop(3))  # removes the last element in the list unless you secify the index #mutate
# lenth = len(marks)
# print(lenth)
# print(marks[0: len(marks) -3])  #slicing the integers cutting the last 3 integers, does not change the original list
# print(marks[0:-3]) #same as above
# print(marks)

#removing an item on the list (removing 40)(specify the value)
# marks.remove(40)    #changes the array
# print(marks)

#Removing t he item using remove function (specify the index))
print(marks.remove(2))


# #adding an item to the list (adds to the end)
# eng = 88
# marks.append(eng)        #Muatates
# print(marks)

# #inserting to a specific index
# marks.insert(2,eng)  # (the index, the value to insert)
# print(marks)

# print( marks * 2) #prints the list twice

#duplicating list
#print(marks * 3)

# adding two list together (combining them)
#print(marks + avarage) #98, 75, 40, 45, 80, 60, 100, 90, 80, 70, 60, 50

#Using .copy does not point to the same memory as the original list, changes in both the original and the copy does not affect the other
# NOT TOO SURE ->Making a copy of a list, when you have a copy, whatever you add to the copy and 
#the original will reflect to the otherlist because they POINT TO THE SAME MEMORY (stores the memory address not the value)
# marks_copy = marks.copy()
# marks_copy.append(43)
# marks.append(99)
# print(marks_copy)
# print(marks)

# #Lists that have different memory pointers
# marks1 = [100, 200, 300]    #this will not be changes by the changes in marks list

#marks -> stores the first item memory address ( 0 )

#Creating copy of the adress using slice
price_list =[1000, 1500,200]
price_list_copy = price_list[:]

price_list.append(43)
price_list_copy.append(99)

print(price_list_copy, price_list )

#Join funstions
subjects=["eng", "math", "science"]
print(" ,".join(subjects))

#sorting a list
print(subjects.sort(reverse=True))
