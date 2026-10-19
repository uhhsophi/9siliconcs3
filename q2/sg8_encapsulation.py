# Creates a class named bankAccount
class bankAccount:
    # Private attributes (hidden from direct outside access)
    def __init__(self, account_number, balance):
        self.__account_number = None
        self.__balance = 0.0

        # Use the setter methods to initialize the values safely
        self.set_account_number(account_number)
        self.set_balance(balance)

    # --- SETTER METHODS ---

    # Public setter for the account number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Public setter for the balance (includes validation check)
    def set_balance(self, balance):
        if balance < 0:
            # If negative, ignore the value and print a warning message
            print("The balance must not be a negative number.")
        else:
            # If zero or positive, update the private balance variable
            self.__balance = balance

    # --- GETTER METHODS ---

    # Public getter property for account number
    @property
    def account_number(self):
        return self.__account_number

    # Public getter property for balance
    @property
    def balance(self):
        return self.__balance


# --- Testing the code ---

# 1. Create a new object of class bankAccount
a1 = bankAccount(12345, 1000)

# Display initial info using the getter properties
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}\n")

# 2. Try to change the balance to a negative number using the setter method
print("Update balance to -100")
a1.set_balance(-100)

# 3. Print the account details again to show the balance stayed at 1000.00
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")
