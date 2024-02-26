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

# #--average for separate classes
# for key, students in classes.items():
#   class_avg = 0
#   for student in students:
#      average = sum(student["grades"])/ len(student["grades"])
#      class_avg += average
#   total_average = class_avg / len(students)
#   print(f"{key} : {total_average: .2f}")

# #--another way
# class_dict = {}
# for key, students in classes.items():
#   class_avg = []
#   for student in students:
#      class_avg.append(sum(student["grades"])/ len(student["grades"]))
#   #print(f"{key}: {sum(class_avg)/len(class_avg): .2f}")
#   class_dict[key] = class_avg
#  # print(class_dict)

# #----task 2
# student_dict ={}
# for key, students in classes.items():
#   dict = {}
#   for student in students:
#      class_avg = sum(student["grades"])/ len(student["grades"])
#      dict[student["name"]] =  class_avg
#      student_dict[key] = dict
#   pprint(student_dict)

# #task 3 task 1+ comprehesion
# class_student_avg = [findAvg(student["grades"] for student in students]

# #---Dictionary comprehension
# #example
# dict = {}
# for key in range(3):
#   dict[key] = key * key

# #output {0: 0, 1: 1, 2: 4}}
# #---Dictionary comprehension
# dict = {key * key for key in range(3)}
# #nested dictionary comprehension
# clc_name = find_avg([find_avg(student["grades"]) for student in students]

# classes_avg = {}

# for cls_name, students in classes.items():

#   classes_avg[cls_name] = find_avg(

#       [find_avg(student['grades']) for student in students])

# print(classes_avg)

# def find_avg(nums):

#   return round(sum(nums) / len(nums), 2)

# classes_avg = {}

# for cls_name, students in classes.items():

#   class_students_avg = []

#   for student in students:

#     class_students_avg.append(find_avg(student['grades']))

#   classes_avg[cls_name] = find_avg(class_students_avg)

# print(classes_avg)


#-Solution
def find_avg(nums):
  return round(sum(nums) / len(nums), 2)


students_avg_dict = {}
for cls_name, students in classes.items():
  students_dict = {}
  for student in students:
    students_dict[student['name']] = find_avg(student['grades'])
  students_avg_dict[cls_name] = students_dict
pprint(students_avg_dict)

#--Task 1(find 1,2,3 pattern ans solve)

students_avg_dict = {}
for cls_name, students in classes.items():
  students_dict = {
      student["name"]: find_avg(student['grades'])
      for student in students
  }
  students_avg_dict[cls_name] = students_dict
pprint(students_avg_dict)

#task 3-> to take it back to the original format
students_avg_dict = {
    cls_name:                    #the key
    {student["name"]: find_avg(student['grades'])   #the value
     for student in students}
    for cls_name, students in classes.items()
}

pprint(students_avg_dict)
