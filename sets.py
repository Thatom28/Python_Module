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

print(indoor_activity.difference(outdoor_activity)) #hiking, swimming (what is different in 1 from 2)

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

print(list(set(colors))) #to convert to a list
#--------------------Activity-----------------
outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

# ---------Task 1
outdoor_gadgets = set()
indoor_gadget = set()
# for key, value in activity_gadgets.items():
#   if value in outdoor_activity:
#     outdoor_gadgets.add(key)
#   elif value in indoor_activities:
#     indoor_gadget.add(key)
    
# print(f"indoor gadget: {indoor_gadget}")
# print(f"outdoor gadgets: {outdoor_gadgets}")

# ---------Task 3: make it neat
# gadget = set()
# def getGadgetSet (activity_gadgets, activities):
#   for gadget, activity in activity_gadgets.items():
#     if activity in activities:
#       gadget.add(gadget)
# print(getGadgetSet(activity_gadgets, indoor_activities))
# print(getGadgetSet(activity_gadgets, outdoor_activities))

# ---------Task 4:set comprehension

def getGadgetSet (activity_gadgets, activities):
  gadget = set()
  for gadget, activity in activity_gadgets.items():
    gadget.add(gadget for gadget in activity_gadgets if activity in activities)
print(getGadgetSet(activity_gadgets, indoor_activities))

#-------corrections
def getGadgetSet (activity_gadgets, activities):
 return gadget = {gadget for gadget,activity in activity_gadgets if activity in activities }
  



