library = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]

# Task 1
# Add Book Function: Write a function add_book(library, new_book) that adds a new book to the library.
# add_book library new_book


#----------------------Task 2----------------------------- 
# Search Books by Author Function: Write a function search_by_author(library, author_name) that returns a list of books by a specific author.

# result = [   
#   {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},  
#   {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False}
#]

#---------------Task 1 Add a new book-------------------
# book ={"title": " Python I", "author": " Lutz", "year": 2014, "available": True}

# def add_book(library, new_book):
#    library.append(new_book)

# #pass by reference therefore it updates the list (no need for return))
# print(add_book(library,book))
# #


#------------------Task 2 search by author-------------------------------
author_books = {}

# def search_author(library, author_name):
#   author_list =[]
#   for book in library:
#     if author_name in book["author"]:
#       author_list.append(book)
#   return author_list

# print(search_author(library, "Mark Lutz"))

##RAGAV SOLUTION

# def search_by_author(library, author_name):
#   return [book for book in library if book["author"] == author_name]

# # pass  #you can use the function it wont give you n error

# print(search_by_author(library, "Mark Lutz"))

#-----------------TASK 3 check avaliabillity-----------------
#you can modify the if statements
# def find_avaliabbillity(library, title):
#   for book in library:
#     if(book["title"] == title and book["available"]):
#       book["available"] = False
#       return f"The book {title} is avaliable, successfully checked out"
#     elif(book["title"] == title and book["available"] == False):
#       return "Book not avaliable"
#     else:
#       return f"{title} is not avaliable in the library"
   
# print(find_avaliabbillity(library, "Fluent "))  

#--------------------------