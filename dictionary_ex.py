books = [
  {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
  {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
  {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
  {"title": "Sapiens", "rating": 4.9, "genre": "History"},
  {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]
#Task 1
book_list = []
for book in books:  #book is the dictionary
  if book["rating"] >= 4.7:
    book_list.append(book["title"])

print(book_list)

#task 2
Top_rated_book = [book["title"] for book in books if book["rating"] >= 4.7]
print(Top_rated_book)

#TASK 3
Top_rated_book = [book["title"] for book in books if book["rating"] >= 4.7]
print(Top_rated_book)
print(sorted(Top_rated_book))
#-------------------------------------------------------------------------------
#TASK 1
inventory = [
  {"name": "Apple", "quantity": 30, "price": 0.50},
  {"name": "Banana", "quantity": 20, "price": 0.20}
]

name = input("what is the product name? ")
quantity = input("what is the quantity? ")
price = input("what is the product price? ")

product = {"name": name, "quantity": quantity, "price": price}
inventory.append(product)
print(inventory)

#TASK 2
name = input("what is the product name? ")
quantity = input("what is the quantity? ")
price = input("what is the product price? ")

for key,value in inventory.items():
  if name == value:
    inventoty[value] = name
  
else:
  product = {"name": name, "quantity": quantity, "price": price}
  inventory.append(product)
print(inventory)