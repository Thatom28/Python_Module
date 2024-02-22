#Lists, Tuple, Dctionary, Sets
#sets - Like List, they are mutable.
#{}
#you cannot have duplicate values in a set
#The order is not guaranteed
tech_gadgets= {"smartphone", "laptop", "smartphone", "tablet","tablet"}  #It will not return duplicate items
print(tech_gadgets)

tech_gadgets.add("E-Reader")  #it can be added anywhere
print(tech_gadgets)

more_gadgets =["drone", 'selfiestick']
tech_gadgets.update(more_gadgets)  #it adds multiple items, it can be from a list or dictionary
tech_gadgets.remove("drone")
print(tech_gadgets)  #gets an error if the item is not in the set

tech_gadgets.discard("monitor")  #it will not give an error if the item is not in the set
print(tech_gadgets)

#----creating a empty set-----
empty_set = set()    
print(empty_set)
empty_set.add("Banana")
print(empty_set)

#------------------------------------
outdoor_activity = { "hiking", "cycling", "swimming"}
indoor_activity = {"reading", "gaming", "cycling"}

print(outdoor_activity.intersection(indoor_activity)) #cycling

print(outdoor_activity.union(indoor_activity)) #hiking, cycling, swimming, reading, gaming

print(indoor_activity.difference(outdoor_activity)) #hiking, swimming

print(outdoor_activity.symmetric_difference(indoor_activity)) #Hiking, swimming, gaming, reading
#-----------------------------------
colors = ["red", "blue", 'red', "green", "pink", "blue"]

set_copy = {*colors}
print(set)
print(set(colors))

#------------The hard way------------
set2 = set()

for color in colors:
  set2.add(color)
print(set2)

print(list(set(colors)))  #to convert to a list