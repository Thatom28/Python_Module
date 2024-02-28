import datetime

transaction_list = [{}]


class Bank:
    trans_id = 0

    # self refers to the object that was requested
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def display_balance(self):
        return f"R{self.balance:,}"

    def withdraw(self, amount, date=datetime.date.today()):
        if self.balance < amount:
            return f"withdrawal amount exceeds the avaliable amount"
        else:
            Bank.trans_id += 1
            self.balance -= amount
            transaction_list.append(
                {
                    "id": Bank.trans_id,
                    "Date": date.strftime("%d %b"),
                    "type": "withdrawal",
                    "amount": self.display_balance(),
                }
            )
            # self.balance -= amount
            return f"Sucess. your balance is: R{self.balance}"

    def deposit(self, amount, date=datetime.date.today()):
        if amount > 0:
            Bank.trans_id += 1
            self.balance += amount
            transaction_list.append(
                {
                    "id": Bank.trans_id,
                    "Date": date.strftime("%d %b"),
                    "type": "deposit",
                    "amount": self.display_balance(),
                }
            )
            return f"Sucess. your balance is now : R{self.balance}"

    def transaction(self):
        for dictionary in transaction_list:
            print("\t".join([f"{key}: {value}" for key, value in dictionary.items()]))


# gemma is an object or instance of bank
gemma = Bank(123, "Gemma Porrill", 5000)
print(gemma.name)

# ---task 2 display  balance
print(f"{gemma.display_balance()}")

# ---Task 3
print(gemma.withdraw(2000))
print(gemma.deposit(7000))
print(gemma.deposit(900))
print(gemma.withdraw(1500))
print(gemma.transaction())
