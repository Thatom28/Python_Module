#Tuple are immutable, they are like lists
#All the operations that are in lists can be used in tuples only those who mutates are not avaliable

person = ("Alex", "SA", 20)

print(person.index("Alex")) #finds the index of the the word
print(person.count("Alex")) #counts the number of times the word appears

#Slicing can be done in a tuple because it does not change the original tuple
#Remove, pop and inserts are not in tuple because they change the list