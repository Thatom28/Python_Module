from pprint import pprint

classes = {
    "Class A": [{
        "name": "Alice",
        "grades": [82, 90, 88]
    }, {
        "name": "Bob",
        "grades": [78, 81, 86]
    }, {
        "name": "Charlie",
        "grades": [85, 85, 87]
    }],
    "Class B": [{
        "name": "Dave",
        "grades": [92, 93, 88]
    }, {
        "name": "Eve",
        "grades": [76, 88, 91]
    }, {
        "name": "Frank",
        "grades": [88, 90, 92]
    }]
}
def find_avg(nums):
  return round(sum(nums) / len(nums), 2)
  
# for cls_name, students in classes.items():
#   cls_ave = []
#   for student in students:
#     student["average"]  = find_avg(student['grades'])
#     cls_ave.append(student['average'])
#   pprint(f'{cls_name}: {find_avg(cls_ave)}')
# pprint(classes)

students_avg_dict = {}
for cls_name, students in classes.items():
  students_dict = {}
  for student in students:
    students_dict[student['name']] = find_avg(student['grades'])
  students_avg_dict[cls_name] = students_dict
#pprint(students_avg_dict)

students_avg_dict = {cls_name:{student['name']:find_avg(student['grades']) for student in students}  for cls_name, students in classes.items()}
pprint(students_avg_dict)

