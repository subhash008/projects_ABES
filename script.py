class BankAccount: 
    def __init__(self, owner, initial_balance): 
        self.owner = owner 
        self.__balance = initial_balance  # Private attribute 
 
    def deposit(self, amount): 
        if amount > 0: 
            self.__balance += amount 
            print(f"Deposited ₹{amount}.") 
        else: 
            print("Invalid deposit amount!") 
 
    def withdraw(self, amount): 
        if 0 < amount <= self.__balance: 
            self.__balance -= amount 
            print(f"Withdrew ₹{amount}.") 
        else: 
            print("Insufficient funds or invalid amount!") 
 
    def check_balance(self): 
        return f"Current Balance: ₹{self.__balance}" 
 
 
account = BankAccount("Priya", 5000) 
account.__balance=50000
account.deposit(1500) 
print(account.check_balance())  # Output: Current Balance: ₹6500 
account.withdraw(2000) 
print(account.check_balance())  # Output: Current Balance: ₹4500