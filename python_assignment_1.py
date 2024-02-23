rooms= [
  {"room_number": 1, "bed_type": "single", "smoking": False, "avaliabillity": False},
  {"room_number": 13, "bed_type": "double", "smoking": True, "avaliabillity": False},
  {"room_number": 22, "bed_type": "single", "smoking": True, "avaliabillity": True},   
  {"room_number": 4, "bed_type": "single", "smoking": True, "avaliabillity": True},    
  {"room_number": 17, "bed_type": "single", "smoking": False, "avaliabillity": False},  
  {"room_number": 20, "bed_type": "double", "smoking": True, "avaliabillity": True},
]

def add_room(rooms, room_number = 1, bed_type = "single", smoking = False):
  for room in rooms :
    if(room["room_number"] is not room_number):
      rooms.append({"room_number": room_number, "bed_type": bed_type, "smoking":smoking})
      return rooms
  return "Room already exists"



def book_room(rooms, preferred_bed_type = "single", smoking_preference= False):
  for room in rooms:
    if room["bed_type"] == preferred_bed_type and room["smoking"] == smoking_preference and room["avaliabillity"] == True:
      room["avaliabillity"] = False
      return f"Room {room['room_number']} is booked"
  return "No room available"

avaliable_list = []
def list_available_rooms(rooms):
  for room in rooms:
    if room["avaliabillity"]:
      avaliable_list.append(room)
      return avaliable_list
  return "No rooms avaliable"
  
# def list_available_rooms2(rooms):
#   avaliable_rooms = [room for room in rooms if room["avaliabillity"]]
#   return avaliable_rooms
  
  
print(add_room(rooms, room_number = 13, bed_type = "double", smoking = True))
print(book_room(rooms, "single", False))
print(list_available_rooms(rooms))