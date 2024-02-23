# nums =[90, 20, 80]

# for num in nums:
#    print(num)
  
# for idx, num in enumerate(nums):#gives you the index and the number (data type= list of tuples)
#    print(idx, num)

employees = [
  {"name": "Alex", "experience": 2},
  {"name": "Gemma"},
  {"name": "Rashay", "experience": 4},
  {"name": "Thato"}
]

#INCREASE THE EXPERIENCE BY 1
# for employee in employees:
#   if employee.get("experience") is None:
#     employee["experience"] = 1
#   else:
#     employee["experience"] += 1

#   if employee["experience"] >= 5:
#     employee["status"] = "Senior"
#   elif employee["experience"] >= 3:
#     employee["status"] = "mid-level"
#   elif employee["experience"] <= 3:
#     employee["status"] = "junior"
      
# print(employees)

#Improves
# for employee in employees:
#   employee["experience"] = employee.get("experience, 0", 0) + 1
#   experience = employee["experience"]

#COPY
movie = {
  "name": "Mr bones",
  "year": 2001
}
movie_copy1= movie.copy()   #cannot add anything else

#unpackiing operator to copy a dictionary
movie_copy2 ={**movie, "rating": 5}   #you can add other keys, the mr bones movie will have a ratings tab
movie_copy3 ={**movie, "rating": 5, "year": 2002}      #Overrides the year
print(movie_copy3)

movie_copy4 = {"rating": 5, "year": 2002, **movie}  #the year will be 2001 since comes after 2002
print(movie_copy4)

movie = {
  "name": "Mr bones",
  "year": 2001
}
detail ={
  "actor": "Leon",
  "director": "mr bones"
}

#combinig the two (make the copies and assign them to the new dictionary
movie_details ={**movie, **detail}
print(movie_details)

#-----------Using unpacking iperator in lists

price = [100, 200, 300]
price_copy =[*price]    #one star
print(price_copy)

price = [100, 200, 300]
price_copy1 =[50, 60,*price, 80]    #one star
print(price_copy1)

t1 =[1, 3]
t2 = [3, 5]
t3 = [*t1, *t2] #combining the lists
print(t3)
