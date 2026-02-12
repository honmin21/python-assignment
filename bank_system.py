import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BankAccount:
    # class variable
    minimum_balance = 1000

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        logging.info("Account created for %s with balance %d", self.name, self.balance)

    # object method
    def deposit_money(self, amount):
        self.balance += amount
        logging.info(
            "Deposit successful | Name: %s | Amount: %d | New Balance: %d",
            self.name, amount, self.balance
        )

    # object method
    def withdraw_money(self, amount):
        if self.balance - amount >= BankAccount.minimum_balance:
            self.balance -= amount
            logging.info(
                "Withdrawal successful | Name: %s | Amount: %d | Remaining Balance: %d",
                self.name, amount, self.balance
            )
        else:
            logging.warning(
                "Withdrawal failed | Name: %s | Balance: %d | Minimum Required: %d",
                self.name, self.balance, BankAccount.minimum_balance
            )

    # object method
    def display_account_details(self):
        logging.info(
            "Account Details | Name: %s | Account No: %s | Balance: %d",
            self.name, self.account_no, self.balance
        )

    # class method
    @classmethod
    def update_minimum_balance(cls, new_balance):
        cls.minimum_balance = new_balance
        logging.info(
            "Minimum balance updated | New Minimum Balance: %d",
            cls.minimum_balance
        )


# Creating objects
acc1 = BankAccount("Srihita", "ACC101", 50000)
acc2 = BankAccount("Jahnavi", "ACC102", 1200)

# Calling methods
acc1.withdraw_money(3000)
acc2.withdraw_money(500)
acc1.deposit_money(2000)
acc1.display_account_details()

# Updating class-level data
BankAccount.update_minimum_balance(2000)
