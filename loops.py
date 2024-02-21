# WHIILE loop
# i = 0

# while i< 3:
#   print(i)      #print i 3 times
#   i = i + 1
# Task 1

# rows = int(input("enter numebr of rows: "))
# i = 1

# while i <= rows:
#   print("😊 " * i)
#   i = i+1


# for i in range(3):   #writes from zero to 2
#   print(i)

# for i in range(1, 3):   #writes from 1, 2 (does nor incude the last one) #the range should be a int therefore tou cant give it a list
#   print(i)

# for i in range(1, 50, 2):   #writes from 1, 3, 5, 7... (does nor incude the last one)
#      print(i)

#Task 2
# rows2 = int(input("enter numebr of rows: "))
# i = 1

# for i in range(1, rows2 + 1):
#    print("😊 " * i)

#Task 3 (multiply each index by 2))
# player_stats =[10, 30, 60]
# player_status_copy = player_stats.copy()

# # for i in range(0,len(player_status_copy)):      
# #   player_status_copy[i] = player_status_copy[i] * 2
# # print(player_stats, player_status_copy)

##The better way to do it
# for stat in player_stats:
#   print(stat)
#   powered_up_stats = [stats * 2 for stat in player_stats ]
# print(powered_up_stats, player_stats)

#Task 4
avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
#count the letter 
# word_count = [len(avenger) for avenger in avengers ]
# print(word_count)

# #count the letters
word_count = [len(avenger) for avenger in avengers ]
for i in range(len(avengers)):
  if(word_count[i] >= 10):  #check the legth of the name at each index
    print(avengers[i])

##Better solution
filter_name =[avenger.upper() for avenger in avengers if len(avenger) >= 10]
print(filter_name)

##To et the lenth of each item in the array
# for avenger in avengers:
#   print(len(avenger))