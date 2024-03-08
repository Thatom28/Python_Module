import json
from pprint import pprint

# data = {
#     "employees": [
#         {"name": "Alice", "age": 30, "department": "Sales"},
#         {"name": "Bob", "age": 25, "department": "Marketing"},
#     ]
# }

# print(data["employees"][0]["age"])

# # json is a multi line string
# # javascript object notation
# data_json = json.dumps(data, indent=4)  # inserting the dictonary in the json file

# # print(data_json["employees"]) #Error

# sport = {"name": "dhoni", "bdl": lambda x: x * 2}  # Function is a first
# print(sport["bdl"(5)])  # to call the lambda function

# # sport_json = json.dumps(sport) #Error -> (JSON SERIALIZABLE) | JSON cannot and covert functions

# Conveting from json to dictionary
student_json = """
{
    "name": "gemma",
    "gender":"female"
}"""
student = json.loads(student_json)
# print(student["name"])

# -----task 1 : active user increase the balance by 10%

bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""
# Using for loop
dict_bank = json.loads(bank_data)

for bank in dict_bank:
    if bank["isActive"]:
        bank["balance"] += bank["balance"] * 0.1

# print as JSON
json_bank = json.dumps(dict_bank, indent=4)  # to separate the key and values
# print(json_bank)

# using list comprehension
dict_bank2 = {
    "balance": bank["balance"] * 0.1 for bank in dict_bank if bank["isActive"]
}
dict_bank.append(dict_bank2)
json_bank2 = json.dumps(dict_bank)
print(json_bank2)
# --------correct list comprehension
# After loading the json

# accounts = [
#     ({**dict_bank, "balance": bank["balance"] * 0.1} if bank["isActive"] else bank)
#     for bank in dict_bank
# ]
# pprint(accounts)

# write a file
with open("bank_account.json", "w") as file:
    json.dump(dict_bank, file, indent=4)
