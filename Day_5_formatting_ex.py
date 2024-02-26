from datetime import datetime

recipe = {
    "name":
    "Spaghetti Carbonara",
    "servings":
    4,
    "ingredients": [
        "200g spaghetti", "100g pancetta", "2 eggs", "1/2 cup grated Parmesan",
        "1 clove garlic"
    ]
}

# Task 1
# ======= Spaghetti Carbonara =======
# - 200g spaghetti
# - 100g pancetta
# - 2 eggs
# - 1/2 cup grated Parmesan
# - 1 clove garlic
# Serves: 4 people
name2 = recipe["name"]
print(f"{name2:=^33}")
for ingredient in recipe["ingredients"]:
  print(f" - {ingredient}")
print(f"Serves: {recipe['servings']} people")

#----Task 2

# Task 2 - Party Invite
# *       Alice       *
# You are invited to the party on March 14, 2024!
# *        Bob        *
# You are invited to the party on March 14, 2024!
# *      Charlie      *
# You are invited to the party on March 14, 2024!

guests = ["Alice", "Bob", "Charlie"]
party_date = datetime(2024, 3, 14)
for guest in guests:
  print(f"{guest:^20}")
  print(f"{guest:^20} you are invited to the party on {party_date:%m %B %y}!")

#-----------multi lined string
about_me = """
Hi, My name is Caleb
I stay in Cape town
"""
print(about_me)  #prints it like it is written(with new lines)
