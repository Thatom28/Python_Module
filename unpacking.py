# #multiple assignment 
# a = b= c = 10
# print(a, b, c)

# Gemma, Dhara, Yolanda = "chacolate" , "Lime", "Vanilla"  #Gemma will be assigned chocolate, Dhara will be assigned lime and Yolanda will be assigned vanilla
# print(Gemma, Dhara, Yolanda)

# #unpacking
# movies = ["remember the titans", "Juno", "Lucy"]
# caleb, gemma , yolanda = movies  
# print(gemma)        #It will print "Juno"

# # t1, t2, t3 = [100, 200, 300, 400]
# # print(t1, t2, t3)    #error because the array is too long

# t1, t2 , t3, _ =[100, 200, 300, 400]    #_ ->skips
# print(t1, t2, t3)  #it will not write 400, this can be inserted in any index

# #Unpaking operator *
# t1, t2 , *t3, =[100, 200, 300, 400, 500, 600, 700]    #get all the remaining values in T3 making it a list
# print(t1, t2, t3)

#UNPACK
# c1, c2, c3, c4 = coordinates 
# dist1 = (c1[0]**2 + c1[1]**2)**0.5
# dist2 = (c2[0]**2 + c2[1]**2)**0.5 
# dist3 = (c3[0]**2 + c3[1]**2)**0.5
# dist4 = (c4[0]**2 + c4[1]**2)**0.5
# print(dist1, dist2, dist3, dist4)

# import math

# coordinates =[(5, 4), (1, 1), (6, 10), (9, 10)]

# distance = []
# for dis in coordinates:
#   print(dis)
#   x, y = dis
#   dis = math.sqrt (x**2 + y**2)
#   #math.sqrt (dis[0]**2 + dis[3]**2)
#   distance.append(dis)
# print(distance)

# #IMPROVED CODE using tuple unpacking directly within the loop
# for x, y in coordinates:
#   distance.append(math.sqrt(x**2 + y**2))
# print(distance)

# #USING LIST COMPREHESION
# distances =[math.sqrt(x**2 + y**2) for x,y in coordinates]

t1, t2, *_,t3 = (100, 200, 300, 400, 60, 40, 30) #skips all the values *_
print(t1, t2, t3)