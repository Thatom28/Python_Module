classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}
#--average for separate classes
for class_name, student in classes.items():
  for st in student:
    average = sum(grade["grades"])/len(grade["grades"])
    print(average)
    
