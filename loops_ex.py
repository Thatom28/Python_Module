numbers =[8, 5, 7, 4,6,2]

numbers_copy =[]
#Type even if the number is divisible by 2 else odd in the list of numbers
result = ["Even" if num % 2 == 0 else "odd" for num in numbers]

print(result)

for i in numbers:
  numbers_copy.append("even" if i% 2 == 0 else "odd")
print(numbers_copy)
  


