class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Enter a valid amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

# --- Main Program Starts Here ---
# Creating an account with dummy data
user_account = BankAccount("1234567890", "1234", 5000)

# Asking for credentials
entered_acc = input("Enter your account number: ")
entered_pin = input("Enter your 4-digit PIN: ")

# Authenticate user
if entered_acc == user_account.account_number and user_account.check_pin(entered_pin):
    print("\nLogin successful!\n")
    
    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            user_account.check_balance()
        elif choice == "2":
            amt = float(input("Enter amount to deposit: ₹"))
            user_account.deposit(amt)
        elif choice == "3":
            amt = float(input("Enter amount to withdraw: ₹"))
            user_account.withdraw(amt)
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid account number or PIN.")
