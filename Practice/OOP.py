class Bank:
    interest_rate = 0.04  # class variable
    bank_acc_num = 0

    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.__balance = balance
        Bank.bank_acc_num += 1

    def display_balance(self):
        return f"R{self.__balance: ,}"

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return f"your balance is now {self.display_balance()}"
        else:
            return "insuffient funds"

    def deposit(self, amount):
        self.__balance += amount
        return f"your balance is now {self.display_balance()}"

    def apply_interest(self):
        self.__balance += self.__balance * Bank.interest_rate
        return self.__balance * Bank.interest_rate

    @classmethod
    def update_interest_rate(cls, value):
        Bank.interest_rate = value

    @staticmethod
    def get_total_num_of_accounts():
        return f"the total number of account is {Bank.bank_acc_num}"


malvin = Bank(100266868, "Malvin Mitchell", 24000)
print(malvin.deposit(400))
print(malvin.withdraw(850))
print(malvin.display_balance())
print(malvin.apply_interest())
print(malvin.update_interest_rate(0.07))
print(malvin.get_total_num_of_accounts())
