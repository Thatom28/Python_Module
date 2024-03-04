# ------Question 1: data sorting and ranking------
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
rank = 1
# Expected Task: Sort the list of dictionaries by grade in descending order and add
# a "rank" key to each dictionary based on the sorting.
students.sort(key=lambda s: s["grade"], reverse=True)
for student in students:
    student["rank"] = rank
    rank += 1
    # print(student)

# -------Question 2: Merging data from two lists
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries
# by matching the "id" field, including all keys.

combined_list = []
for employee in employees:
    for salary in salaries:
        if employee["id"] == salary["id"]:
            combined_list = {**employee, **salary}
    # print(combined_list)

# using list comprehension
combined_list = [
    {**employee, **salary}
    for employee in employees
    for salary in salaries
    if employee["id"] == salary["id"]
]
# print(combined_list)

# ---------Question 3: advanced filtering with multiple conditions
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in
# the "Electronics" category with a price less than 500.
filtered_product = []
for product in products:
    if product["category"] == "Electronics" and product["price"] < 500:
        filtered_product.append(product)
# print(filtered_product)

# using list comprehension
filtered_product = [
    product
    for product in products
    if product["category"] == "Electronics" and product["price"] < 500
]
# print(filtered_product)

# -------Question 4: Complex data transformation
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are
# total quantities ordered across all orders.
prod_dict = {}
for order in orders:
    for product in order["items"]:
        product_name = product["product"]
        product_quantity = product["quantity"]
        if product_name not in prod_dict:
            prod_dict[product_name] = product_quantity
        else:
            prod_dict[product_name] += product_quantity
# check if keys are identical add onto it
# print(prod_dict)

# -----Question 5:Consolidation and Summarization
summary = {}
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.
for transaction in transactions:
    amount = transaction["amount"]
    category = transaction["category"]
    if category in summary:
        summary[category] += amount
    else:
        summary[category] = amount

# print(summary)

# -------Question 6: Grouping and Aggregating Data
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and
# calculate the total sales amount for each.
grouping = {}
for sale in sales:
    salesperson = sale["salesperson"]
    amount = sale["amount"]
    if salesperson not in grouping:
        grouping[salesperson] = amount
    else:
        grouping[salesperson] += amount
# print(grouping)


# --------Qustion 7:Lambda Functions for Spell Power
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending
# order using a lambda function
spells.sort(key=lambda x: x[1], reverse=True)
# print(spells)

# ---------Question 8: Map Transformation for Potion Ingredients
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.
grams = list(map(lambda x: x + ": 3 grams", ingredients))
# print(grams)

# ---------Qustion 9: Magical Book Filter and Formatter
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# Expected Task: Filter books with more than 120 pages and
# format their titles to uppercase.
filtered_list = [
    {"title": book["title"].upper(), "pages": book["pages"]}
    for book in books
    if book["pages"] > 120
]
# print(filtered_list)


# ---------Qustion 10: Wizard Duel Game Class
class WizardDuel:
    # Expected Task: Implement a class with methods for casting spells,
    # reducing health points, and determining the winner
    def __init__(self, spell, health_points):
        self.spell = spell
        self.health_points = health_points

    def cast_spell(self):
        pass

    def reduce_health_points(self):
        pass

    def deter_winner(self, health_points):
        pass


# ---------Question 11: Custom Error Handling in Potion Making

# ---------Question 12: Hogwarts Library Database Query
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.
book_filter = [book for book in library if book["author"] == "Bathilda Bagshot"]
# print(book_filter)

# ---------Question 13: Hogwarts House Points Calculator
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]
# Expected Task: Aggregate points for each house and print the total.

total_points = {}
for house in house_points:
    house_name = house["house"]
    no_points = house["points"]
    if house_name not in total_points:
        total_points[house_name] = no_points
    else:
        total_points[house_name] += no_points

# print(total_points)


# ---------Question 14: Class Inheritance for Magical Creatures

# ---------Question 15: Custom Sorting with Lambda for Magical Artifacts
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.
sorted_by_age = [artifacts.sort(key=lambda artifact: artifact["age"])]
sorted_by_power = sorted_by_age.sort(key=lambda x: x["power"])
print(artifacts)  # fix
