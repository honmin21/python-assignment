import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class recharge:
    recharge_plan = 899
    validity = 44  # validity in days

    def __init__(self, mobile_no, balance, validity_days):
        self.mobile_no = mobile_no
        self.balance = balance
        self.validity_days = validity_days
        logging.info(
            "Account created | Mobile No: %s | Balance: %d | Validity: %d days",
            self.mobile_no, self.balance, self.validity_days
        )

    def dorecharge(self):
        self.balance += recharge.recharge_plan
        self.validity_days = recharge.validity
        logging.info(
            "Recharge successful | Mobile No: %s | New Balance: %d | Validity: %d days",
            self.mobile_no, self.balance, self.validity_days
        )

    def checkvalidity(self):
        logging.info(
            "Validity checked | Mobile No: %s | Validity: %d days",
            self.mobile_no, self.validity_days
        )

    def showbalance(self):
        logging.info(
            "Balance checked | Mobile No: %s | Balance: %d",
            self.mobile_no, self.balance
        )

    @classmethod
    def updateplans(cls, new_plan, new_validity):
        cls.recharge_plan = new_plan
        cls.validity = new_validity
        logging.info(
            "Recharge plans updated | New Plan Amount: %d | New Validity: %d days",
            cls.recharge_plan, cls.validity
        )
# Create recharge accounts
user1 = recharge(mobile_no="9876543210", balance=200, validity_days=10)
user2 = recharge(mobile_no="9123456789", balance=50, validity_days=5)

# Show initial balance and validity
user1.showbalance()
user1.checkvalidity()

# Perform recharge
user1.dorecharge()

# Check balance and validity after recharge
user1.showbalance()
user1.checkvalidity()

# Update recharge plans
recharge.updateplans(999, 56)

# Recharge another user with updated plan
user2.dorecharge()
user2.showbalance()
user2.checkvalidity()
