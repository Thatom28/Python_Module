prince = 100

def get_price():
    print("the price is : ", prince)

#get_price()

#Lexical scope: the inner loop can use the upper loop but the outer loop cannot use the inner loop
def market():
    price = 100
    def get_price():
     print("the price is : ", prince)

get_price()
#print(market())

# Scope -Lifetime of a variable, the x cannot be called outside the function
# def cool():
#    x =10

# cool()
# print(x)  # x is not defined

# closure = own scope + lexical scpe
code_word = 'Hulk'
def space_ship():
   question = "Please provide code word"

   def code_word_check():
      password="Hulk"
      print(question)

      if (password == code_word):
         print(f"Welcome , {password} the strogest avenger💪")
      else: 
         print("❌Access denied to r🚀")
      code_word_check()     #you need to call the fuction you defined insdide the function because it does not mean it will automatically run
   
#space_ship()

#add1 can be able to accessed because of closure scope
def add(x):
   def add1(y):
      return x+ y
   return add1

#default value copy by reference : all teh fun called will populate the same list, this is reference
# def fun(nums = []):
#    nums.append(10)
#    print(nums)
# fun()
# fun()
# fun()

# def fun():
#     nums = []
#     nums.append(10)
#     print(nums)
#     nums.pop()

# fun()
# fun()


# def fun(nums = []):
#     nums.append(10)
#     print(nums)
#     nums.pop()

# fun()
# fun()

def fun(nums = ()):
    if nums is ():
        nums.append(10)
    print(nums)

fun()
fun()

#solution
def fun(nums = None):
   if nums is None:
    nums = []
   print(nums)

fun()
fun()

# == is a binary operator and in is a memory operator 