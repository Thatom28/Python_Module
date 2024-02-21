# Dictionary -> HashMap -> key:Value
#keys should be unique
# Lists -> []
#tuple -> Tuple
#Dictionary -> {}

person = {
  "name": "Siya Kolisi",
  "age": 32,
  "country": "South Africa",
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
