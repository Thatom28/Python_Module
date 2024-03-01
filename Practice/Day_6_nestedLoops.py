classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]},
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]},
    ],
}


def find_avg(nums):
    return round(sum(nums) / len(nums), 2)


# Initialize a dictionary for class averages
student_avg_dic = {}
# Iterate over each class
for class_name, students in classes.items():
    student_dict = {}  # 1
    # calculate each student's average
    for student in students:  # 3
        student_dict[student["name"]] = find_avg(student["grades"])  # 2
        student_avg_dic[class_name] = student_dict
print(student_avg_dic)

# 123 Pattern
student_avg_dic = {}
for class_name, students in classes.items():  # 3
    student_dict = {
        student["name"]: find_avg(student["grades"]) for student in students  # 2
    }
    student_avg_dic[class_name] = student_dict  # 1
print(student_avg_dic)

# outer 123
student_avg_dic = {
    class_name: {student["name"]: find_avg(student["grades"]) for student in students}
    for class_name, students in classes.items()
}
print(student_avg_dic)

# ---------------finding class average-------Verbose approach
summary = {}
for class_name, students in classes.items():
    class_avg = []
    for student in students:
        class_avg.append(find_avg(student["grades"]))
    summary[class_name] = find_avg(class_avg)
print(summary)
# ---Inner 123
summary = {}
for class_name, students in classes.items():
    class_avg = [find_avg(student["grades"]) for student in students]
    summary[class_name] = find_avg(class_avg)
print(summary)

# ---Outer 123 -> list comprehension (writing the solution in a more concise way)
summary = {class_name: find_avg(class_avg) for class_name, students in classes.items()}
print(summary)
