# books = [
#   {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
#   {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
#   {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
#   {"title": "Sapiens", "rating": 4.9, "genre": "History"},
#   {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
# ]
# #Task 1
# book_list = []
# for book in books:  #book is the dictionary
#   if book["rating"] >= 4.7:
#     book_list.append(book["title"])

# print(book_list)

# #task 2
# Top_rated_book = [book["title"] for book in books if book["rating"] >= 4.7]
# print(Top_rated_book)

# #TASK 3
# Top_rated_book = [book["title"] for book in books if book["rating"] >= 4.7]
# print(Top_rated_book)
# print(sorted(Top_rated_book))
#-------------------------------------------------------------------------------
# #TASK 1
# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# # name = input("what is the product name? ")
# # quantity = int(input("what is the quantity? "))
# # price = float(input("what is the product price? "))

# # product = {"name": name, "quantity": quantity, "price": price}
# # inventory.append(product)
# # print(inventory)

# #TASK 2
# name = input("what is the product name? ")
# new_quantity = int(input("what is the quantity? "))
# price = float(input("what is the product price? "))


# for product in inventory:    #getting the dictionaries out of the list
#   for key,value in product.items():
#     if name == value:
#       product["quantity"] += new_quantity
#       product['price']  += price
#       break
# else:
#   product = {"name": name, "quantity": new_quantity, "price": price}
#   inventory.append(product)
# print(inventory)

# #ragav solution
# new_product = {"name": name, "quantity": new_quantity, "price": price}

# item_found =False  #flag

# for item in inventory:
#   if item["name"] == new_product["name"]:
#     item["quantity"]  += new_quantity
#     item["price"] = price
#     item_found =True;
#     break
# if(item_found == False):   #or if(not item_found):
#     inventory.append(new_product)
# print(inventory)

## TASK 3
# Output
# People who are 21 or above and VIP123
# Blacklist are not allowed

# ["Alice", "Charlie"]
guests = [
  {"name": "Alice", "age": 25, "code": "VIP123"},
  {"name": "Bob", "age": 17, "code": "VIP123"},
  {"name": "Charlie", "age": 30, "code": "VIP123"},
  {"name": "Dave", "age": 22, "code": "GUEST"},
  {"name": "Eve", "age": 29, "code": "VIP123"}
]

blacklist = ["Dave", "Eve"]

guest_list = []

# for guest in guests:
#   if (guest["age"] > 21 and guest["code"] == "VIP123" and guest["name"] not in blacklist):
#     guest_list.append(guest["name"])

# print(guest_list)

guest_list =[guest["name"] for guest in guests if guest["age"] > 21 and guest["code"] == "VIP123" and guest["name"] not in blacklist]    #it inserts the name already threfore no need to append
print(guest_list)


