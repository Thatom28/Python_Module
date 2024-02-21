# Dictionary -> HashMap -> key:Value
#keys should be unique
# Lists -> []
#tuple -> Tuple
#Dictionary -> {}

person = {
  "name": "Siya Kolisi",
  "age": 32,
  "country": "South Africa",
  "address" : {
    "city" : "Port elizabeth",
    "country": "south africa"
  },
  "height" : 186,
  "school": "Grey high school",
  "sport": "Ruby"
}

print(person, type(person))
print(person["name"]) #To get the name
person["age"] += 1 #To add 1 to the age
print(person) #To get the age and add 1 

#METHODS AVALIABLE
#Iterable -> list, tuple, dict_keys
print(person.keys())  #shows the keys : name, age, country, sport
print(person.values())  #shows the values : Siya Kolisi, 32, South Africa, Ruby
print(person.items())   #gives you the list of tuple (name, Siya Kolisi)) (Used with a for loop)

for details in person.items():  #returns the list of keys and values
  print(details)
#IMPROVED
for key, value in person.items():
  print(key,value)


#Safety for your values (get)

#print(person["height"])    #will  have an error since there is no key named height

#how to fix it
print(person.get("height")) #will return none

#Adding a (key, value) (you get the value in the dictionary if it is not written)
print(person["height"], 174)  #returns none 174

print(person['address']["city"])  #in a nested dictionary, to get a value of the 2nd layer
print(person["address"].get("city"))    #.get, gets the value out of the object

#NB: none types cannot be used with get
#To use it
print(person.get("stats",{}).get("points"))   #returns None and does not break the code

#------DICTIONARY COMPREHENSION-----

nums = {x :x for x in range(10)}     #X:x is the key and teh value
print(nums)

nums = {x:x for x in range(10) if x % 2 == 0}
print(nums)
