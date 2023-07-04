class BankAccount():

    InterestRate = 0.05
    DailyWithdrawLimit = 5000

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdrawal_transactions(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds!")

    def deposit_transactions(self, amount):
        self.balance += amount

    def display_balance(self):
        print("Account Number: ",self.account_number)
        print("Balance: ",self.balance)


class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if super().DailyWithdrawLimit < amount:
            print("Daily withdrawal limit reached. Transaction blocked.")
            return
        else:
            super().withdrawal_transactions(amount)
    
    def deposit(self, amount):
        super().deposit_transactions(amount)

    def calculate_interest(self):
        interest = self.balance * super().InterestRate
        print(f"Interest you get on your account balance: {interest}")


# Driver Code:
savings_account = SavingsAccount("123456789", 0)

while True:
    print("\n\n\n")
    print("========Welcome to XYZ BANK========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Calculate Interest")
    print("4. Display Account Balance")
    print("5. Exit")

    inp = input("Enter Option (1-5): ")

    if inp == "1":
        amount = int(input("Enter the deposit amount: "))
        savings_account.deposit(amount)
        print("Deposit successful.")

    elif inp == "2":
        amount = int(input("Enter the withdrawal amount: "))
        savings_account.withdraw(amount)

    elif inp == "3":
        savings_account.calculate_interest()

    elif inp == "4":
        savings_account.display_balance()

    elif inp == "5":
        print("THANK YOU FOR CHOOSING XYZ BANK")
        break

    else:
        print("Invalid Option Selected! Try Again")