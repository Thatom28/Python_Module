#Lamda functions
#used when you want to pass a function as an argument(parameter)
#They are first class citizens

#1. assign a function as a variable
#2. pass a function as an argument
#3. return a function

#-----------first example-------(name)(parameters)(function body)
# add = lambda a, b: a+b
# print(add(2,3))

# def fun(y):    #function named fun that takes 1 parameter
#   x=4
#   return x +y

# print(fun(2))      # 4+ 2

#map(function, list)
# double_stats = map(lambda x: x *2, [10,20,30])  #[20,40,60]]

# print(list(double_stats))  #return a list

# #you can add any function to a map
# def square(x):
#   return x*x
# squares = map(square, [1,2,3,4,5])
# print(list(squares))

#----------------------------------------------------
# def say_hello():
#   return "hello,"

# def greeting(hello_message, name):
#   return (hello_message() + name)

# print(say_hello, "caleb")  #say_hello does not need to be a function



#--------------------------------Task 1-----------------------
def map_own(fn, arr):
   return list(map(fn, arr))
  
print(map_own(lambda x : x * 2, [10, 30, 60]))

#return [fn(n) for n in arr]   #Instead of map

#-------------------Returning a fuction as an argument---------
def sayHello1():
  def msg():
    return 'Hello, 🎊'
  return msg    #returning a function as an argument
print(sayHello1()())  #to print the function that is  inside another function

#another way of returning a nested function
msg_function = sayHello1()    #because it returns the function msg
print(msg_function())

#-------------print 18 using the function------------
mul = lambda x: lambda y: x * y  #same as def LamdaX(lamday , x,y)
print(mul(2)(3))    #like above you get both functions

#---step by step
mul2 = lambda x: lambda y: x * y 
mul67 = mul(67)  #[67 * y]
mul9 = mul67(9)  #[67 * 9]
print(mul9)

#-------------------------FILTERS---------------------
# filter is a HOF-. it takes a function as an argument
result1 = map(lambda x: x*x, [10,20,30])
result2 = filter(lambda x: x > 10 , [10,2,33,4,54,6,7,8])
print(list(result2))

#------------Sequencing----
#sequence - list (methods avaliable)
# 1. len
# 2.sum
# 3.sorted
print(sum([10,30,20,7]))
print(max([10,30,20,7]))
print(min([10,30,20,7]))

print(all([True, False, True]))  #false the return a boolean
print(any([True, False, True]))  #true returns a boolean