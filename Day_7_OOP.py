
#Object orientated programming
#why OOP was created :modelling things as real word objects
#i.e  car -> engine, wheels, doors, 
#you want to create multiple objects of a car that have different implimentations

# class Car:

# #init function -> it is called first like a constructor
#     # def __init__(self):
#     #     self.name = "ferrari"
#     #     self.engine= "V8"
#     #     self.wheels= 4
#     #     self.doors= 2
        
# # ferrari = Car()   #The values will always be the ones in the init

# # #Not DRY why __init__ is used
# # ferrari = Car()
# # ferrari.name = "ferrari"
# # ferrari.engine= "V8"
# # ferrari.wheels= 4
# # ferrari.doors= 2

# # toyota = Car()
# # toyota.name = "toyota"
# # toyota.engine= "V4"
# # toyota.wheels= 4
# # toyota.doors= 4
# #-----------------Better way
#  def __init__(self, name, engine, wheels, doors):
#         self.name = name
#         self.engine= engine
#         self.wheels= wheels
#         self.doors= doors

#  def horn(self):
#     return "Vroom vroom"
 
# ferrari = Car("ferrari", "V8", 4, 2)
# toyota = Car("toyota", "V4", 4, 4)
# mazda = Car("mazda", "V3", 4, 5)
# suzuki = Car("suzuki", "V2", 4, 2)

# print(mazda.name, mazda.engine)
# print(ferrari.horn())

#-------Task model a bank account
# import datetime

# transaction_list =[{}]
# trans_id = 0
# class Bank:
#self refres to the object that was requested
#  def __init__(self, account_num, name, balance):
#     self.account_num = account_num
#     self.name = name
#     self.balance = balance

#  def display_balance(self):
#     return f"your balance is R{self.balance:,}"

 
#  def withdraw(self, amount, date = datetime.date.today()):
#     global trans_id
#     if self.balance < amount:
#         return f'withdrawal amount exceeds the avaliable amount'
#     else:
#         trans_id += 1
#         transaction_list.append({"id": trans_id,"Date": date.strftime("%d %b %Y"), "type": "withdrawal", "amount": self.display_balance()})
#         self.balance -= amount
#         return f'Sucess. your balance is: R{self.display_balance()}'
    
#  def deposit(self, amount, date = datetime.date.today()):
#         if amount > 0:
#          global trans_id
#          trans_id += 1
#          transaction_list.append({"id": trans_id,"Date": date.strftime("%d %b %Y"), "type": "deposit", "amount": self.display_balance()})
#          self.balance += amount
#          return f'Sucess. your balance is now : R{self.display_balance()}'

#  def transaction(self):
   #  for dictionary in transaction_list: 
   #   print("\t".join([f"{key}: {value}" for key, value in dictionary.items()]))


#gemma is an object or instance of bank
# gemma = Bank(123, "Gemma Porrill", 5000)
# print(gemma.name)

# #---task 2display  balance
# print(f'{gemma.display_balance()}')

# #---Task 3
# print(gemma.withdraw(2000))
# print(gemma.deposit(7000))
# print(gemma.deposit(900))
# # for dictionary in transaction_list:
# #  print(dictionary)
# print(gemma.transaction())
     


#ENCAPSULATION -> putting in all together in one container -> giving access to specific methods
# class Bank1:

#    interest_rate = 0.02
#    def __init__(self, account_num, name, balance):
#       self.account_num = account_num
#       self.name = name
#       #__ private viraible
#       self.balance = balance      

#    def display_balance(self):
#       return f"your balance is R{self.balance:,}"

   
#    def withdraw(self, amount):
#       global trans_id
#       if self.balance < amount:
#          return f'withdrawal amount exceeds the avaliable amount'
#       else:
#          self.balance -= amount
#          return f'Sucess. your balance is: R{self.display_balance()}'
      
#    def deposit(self, amount):
#          if amount > 0:
#             self.balance += amount
#             return f'Sucess. your balance is now : R{self.display_balance()}'

#    def apply_interest(self):
#       self.balance += self.balance * Bank1.interest_rate
#       return self.display_balance()

# gemma = Bank1(123, "Gemma Porrill", 5000)
# dhara = Bank1(134, "Dhara Khara", 15000)

# #print(gemma.__balance)
# print(gemma.apply_interest()) 




#ENCAPSULATION -> putting in all together in one container -> giving access to specific methods
# class Bank3:

#    interest_rate = 0.02
#    count_acc = 0
#    def __init__(self, account_num, name, balance):
#       self.account_num = account_num
#       self.name = name
#       #__ private viraible
#       self.__balance = balance      
#       Bank3.count_acc += 1

# #used when we update
#    @classmethod  #points to the class
#    def update_interest_rate(cls, rate):  
#       Bank3.interest_rate = rate
# #dont use the class method if you are not updating
#    # @classmethod
#    # def  get_total_no_accounts(cls):
#    #    return f'{Bank3.count_acc} accounts created' 
   
#    #-static methods -> no class and self
#    @staticmethod
#    def  get_total_no_accounts():
#       return f'{Bank3.count_acc} accounts created' 
   

#    def display_balance(self):
#       return f"your balance is R{self.__balance:,}"

   
#    def withdraw(self, amount):
#       global trans_id
#       if self.__balance < amount:
#          return f'withdrawal amount exceeds the avaliable amount'
#       else:
#          self.__balance -= amount
#          return f'Sucess. your balance is: R{self.display_balance()}'
      
#    def deposit(self, amount):
#          if amount > 0:
#             self.__balance += amount
#             return f'Sucess. your balance is now : R{self.display_balance()}'

#    def apply_interest(self):
#       self.__balance += self.__balance * Bank3.interest_rate
#       return self.display_balance()

# gemma = Bank3(123, "Gemma Porrill", 5000)
# dhara = Bank3(134, "Dhara Khara", 15000)

# Bank3.update_interest_rate
# #you cannot use this method you can access by a method display balance
# #print(gemma.__balance)
# print(gemma.display_balance())
# print(gemma.apply_interest()) 
# # print(Bank3.get_total_no_accounts())
# print(gemma.get_total_no_accounts())

class Bank3:

   interest_rate = 0.02
   count_acc = 0
   def __init__(self, account_num, name, balance):
      self.account_num = account_num
      self.name = name
      #__ private viraible
      self.__balance = balance      
      Bank3.count_acc += 1

#used when we update
   @classmethod  #points to the class
   def update_interest_rate(cls, rate):  
      Bank3.interest_rate = rate
#dont use the class method if you are not updating
   # @classmethod
   # def  get_total_no_accounts(cls):
   #    return f'{Bank3.count_acc} accounts created' 
   
   #-static methods -> no class and self
   @staticmethod
   def  get_total_no_accounts():
      return f'{Bank3.count_acc} accounts created' 
   

   def display_balance(self):
      return f"your balance is R{self.__balance:,}"

   
   def withdraw(self, amount):
      global trans_id
      if self.__balance < amount:
         return f'withdrawal amount exceeds the avaliable amount'
      else:
         self.__balance -= amount
         return f'Sucess. your balance is: R{self.display_balance()}'
      
   def deposit(self, amount):
         if amount > 0:
            self.__balance += amount
            return f'Sucess. your balance is now : R{self.display_balance()}'

   def apply_interest(self):
      self.__balance += self.__balance * self.interest_rate  #Use this to call the interest of the class
      return self.display_balance()
   
   def get_balance  (self):
      return self.__balance
   
   def update(self, amount):
      self.__balance += amount

gemma = Bank3(123, "Gemma Porrill", 5000)
dhara = Bank3(134, "Dhara Khara", 15000)

Bank3.update_interest_rate
#you cannot use this method you can access by a method display balance
#print(gemma.__balance)
print(gemma.display_balance())
print(gemma.apply_interest()) 
# print(Bank3.get_total_no_accounts())
print(gemma.get_total_no_accounts())



#task 1 - apply interest should be 0.5

class SavingsAccount(Bank3):
   interest_rate = 0.05
   # def __init__(self, account_num, name, balance):
   #    super().__init__(account_num, name, balance)

   # def apply_interest(self):
   #    return self.get_balance() * self.interest_rate
   
   # def applyInterest(self):
   #    self.update()   

       

class CheckingAccount(Bank3):
     transaction_fee = 1
     def withdraw(self, amount):
      total_amount = amount + 1
      return super().withdraw(total_amount)

 
# # SavingsAccount -  interest_rate = 0.05
 
# # Task 1
gemma = SavingsAccount(123, "Gemma Porrill", 1_000)
print(gemma.name)
gemma.apply_interest()
print(gemma.display_balance())  # 1_050
 
# # Task 2
# # CheckingAccount - withdraw  R1
alex = CheckingAccount(126, "Alex Lazarus", 100)
print(alex.withdraw(50))
# #  49

#magic methods:  __repr__ and __str__
def __str__(self):
   return f'this Account belongs to {self.name}'
print(gemma)