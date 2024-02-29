# Property function in a built in function that enables you to ceate a special type of attribute called a property for a class
# they are used to encapsulate the access to object attribute and to add logic to a process
# Property function allows a method to be accesses an an attribute instead of a method.


class Student:
    #     students = []

    def __init__(self, fullname, course, module):
        self._fullname = fullname
        self.course = course
        self.module = module

    # since the fullname property is protected it cannot be accessed outside the scope of the class
    # we create a get_fullname function that returns the full name of teh instance
    @property  # whatever is created here is considered a property and everytime we want to access it, it will call these method
    def full_name(self):
        print(f"{self._fullname} is accessed")
        return self._fullname

    @full_name.setter  # can use a getter, setter and deleter, allows you to mutate a variable
    def full_name(self, value):
        print(
            f"{self._fullname} is now {value}"
        )  # replacing the _fullname with the new value
        self._fullname = value

    @full_name.deleter
    def full_name(self):
        print(f"{self._fullname} is deleted")
        del self._fullname


lee = Student("lee jones", "computer science", "intro to python")
print(lee.full_name)
lee.full_name = "Thato m"
print(lee.full_name)

del lee.full_name
# print(lee.full_name)  # returns an error because fullname is now deleted


class Bank:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self._balance = balance

    def withdraw(self, amount):
        if self._balance < amount:
            return f"withdrawal amount exceeds the avaliable amount"
        else:
            self._balance -= amount
            return f"Sucess. your balance is: R{self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Sucess. your balance is now : R{self._balance}"

    # whatever is created here is considered a property and everytime we want to access it, it will have access to all these methods.
    @property
    def balance(self):
        print(f"{self._balance} is accessed")

    # If you assign a new value to balance, this method will be executed
    @balance.setter
    def balance(self, value):
        print(f"balance is now {value}")

    # If you delete balance, this method will be executed. and you cannot print balance again because it has been removed from memory
    @balance.deleter
    def balance(self):
        print(f"{self._balance} has been deleted")
        del self._balance


gemma = Bank(1234, 4500)
print(gemma.acc_num)
print(gemma._balance)
gemma.balance = gemma.withdraw(500)
print(gemma.balance)

# ---------Decorators------------
# Decorators allows you to modify the behaviour of a function or class without modifying altering their code
# I am changing  the return type of the divide() function from float to int

# --------Creating a decorator using a function
from functools import wraps


class Calculation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def my_decorator(func):
        def wrapper(
            self, *args, **kwargs
        ):  # can take arguments and keywords, this gets arguments from the divide method,
            # this allows the method to add more arguments
            result = func(self, *args, **kwargs)
            print(
                f"the data type of {result} is {type(result)}"
            )  # type the return type of the function
            print(f"Converted result to an integer: {int(result)}")

        return wrapper

    @my_decorator  # the my-decorator is applied to this method, but can be  applied to any other method
    def divide(self):
        return float(self.num1 / self.num2)


calc1 = Calculation(678, 56)
print(calc1.divide())
print(calc1.divide())  # applying the decorator to the divide function


# ------------Creating a decorator using a class
class decorator_class:
    def __init__(self, func):
        self.func = func  # returns an instance of the function

    def __call__(self):
        result = self.func()
        print(
            f"the data type of {result} is {type(result)}"
        )  # type the return type of the function
        print(f"Converted result to an integer {int(result)}")


@decorator_class
def divide(num1, num2):
    return num1 / num2


divide(56 / 6)
