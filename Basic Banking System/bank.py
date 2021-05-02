class Account:

    total_account_count = 0

    def __init__(self, account_number, balance):
        self.bank_name = "HBL"
        self.account_number = account_number
        self.limit = 500000
        self.balance = balance
        Account.total_account_count += 1

    def get_limit(self,):
        return self.limit

    def set_limit(self, new):
        self.limit = new

    def get_details(self):
        print("Bank Name: " + self.bank_name)
        print("Account Number:  {}".format(self.account_number))
        print("Limit: {}".format(self.limit))
        print("Balance: {}".format(self.balance))

    def get_total_account_count(self):
        return Account.total_account_count

    def change_bank(self, new):
        self.bank = new

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        if self.balance + amount > self.limit:
            return False
        else:
            self.balance += amount
            return True

    def transfer(self, amount, another):
        if self.balance > amount:
            self.balance -= amount
            return True
        else:
            return False


acc1 = Account(123, 500900)
acc2 = Account(456, 85000)
acc3 = Account(789, 9000)


if acc1.withdraw(6000):
    print("amount withdrawn")
else:
    print("amount Can't be withdrawn")


if acc2.deposit(9000):
    print("Amount deposited")
else:
    print("Amount can't be deposit")


if acc2.transfer(9000, 123):
    print("Amount transfered")
else:
    print("Amount can't be transfered")


acc1.get_details()

print("Number Of Accounts : {}".format(acc1.get_total_account_count()))
