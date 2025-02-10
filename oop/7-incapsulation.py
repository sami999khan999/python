# Encapsulation Example:
# Encapsulation restricts direct access to an object's internal data and methods,
# exposing only what is necessary. In this example, the BankAccount class hides the
# account balance (using a private attribute) and provides public methods to interact with it.


class BankAccount:
    # Constructor initializes the account holder and the private balance.
    def __init__(self, account_holder: str, initial_balance: float):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute: cannot be accessed directly outside the class.

    # Public method to deposit money. Ensures only valid (positive) amounts are added.
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money. Checks for positive amount and sufficient funds.
    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    # Public method to retrieve the current balance.
    def get_balance(self):
        return f"Available Balance: ${self.__balance:.2f}"

    # Private method: internal operation not intended for public use.
    def __private_method(self):
        return "This is a private operation."


# Example Usage:
account = BankAccount("John Doe", 1000.0)
print(account.get_balance())  # Output: Available Balance: $1000.00

account.deposit(500)  # Output: $500 deposited successfully.
print(account.get_balance())  # Output: Available Balance: $1500.00

account.withdraw(200)  # Output: Insufficient balance.
account.withdraw(300)  # Output: $300 withdrawn successfully.
print(account.get_balance())  # Output: Available Balance: $1200.00

# Direct access to the private attribute will result in an error:
# print(account.__balance)   # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing the private method using name mangling (not recommended in practice):
print(account._BankAccount__private_method())  # Output: This is a private operation.

# Summary:
# - Encapsulation hides internal details (like __balance) from direct external access.
# - Public methods (deposit, withdraw, get_balance) provide controlled interaction with private data.
# - This ensures data integrity and prevents unintended modifications.
