name = input("Enter name: ")
email = input("Enter email: ")
meal = input("vegetarian or non-vegetarian: ")
accomodation = input("need accomodation?:")

Registered_participants = []


def register_participant(name,
                         email,
                         meal_preference="non-vegetarian",
                         needs_accommodation=False):
  if (meal_preference == ""):
    meal_preference = "non-vegetarian"
  participant = {
      "name": name,
      "email": email,
      "meal_preference": meal_preference,
      "needs_accomodation": needs_accommodation
  }
  Registered_participants.append(participant)
  print(Registered_participants)


register_participant(name, email, meal, bool(accomodation))
