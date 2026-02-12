import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class eorder:
    tax_percentage = 5

    # constructor
    def __init__(self, order_id, customer_name, customer_address, customer_phoneno, price, quantity):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phoneno = customer_phoneno
        self.price = price
        self.quantity = quantity
        self.orderplaced = False
        self.ordercancelled = False
        logging.info("Order created | Order ID: %s | Customer: %s", self.order_id, self.customer_name)

    # object method for placing order
    def place_order(self):
        self.orderplaced = True
        self.ordercancelled = False
        logging.info("Order of Order ID %s is placed successfully", self.order_id)

    # object method for cancelling order
    def cancel_order(self):
        if self.orderplaced:
            self.ordercancelled = True
            logging.info("Order for Order ID %s is cancelled successfully", self.order_id)
        else:
            logging.info("Order was not placed yet | Order ID: %s", self.order_id)

    # object method to calculate price with tax
    def calculateprice(self):
        subtotal = self.price * self.quantity
        tax_amount = (subtotal * eorder.tax_percentage) / 100
        total_price = subtotal + tax_amount
        logging.info("Total price with tax for Order ID %s: %.2f", self.order_id, total_price)

    # class method to update tax
    @classmethod
    def update_tax(cls, new_tax):
        cls.tax_percentage = new_tax
        logging.info("New tax percentage updated: %d%%", cls.tax_percentage)
# Example usage of eorder class

# Create orders
order1 = eorder(
    order_id=201,
    customer_name="srihita",
    customer_address="123 Main St",
    customer_phoneno="555-1234",
    price=100,
    quantity=2
)

order2 = eorder(
    order_id=202,
    customer_name="jahnavi",
    customer_address="456 Park Ave",
    customer_phoneno="555-5678",
    price=50,
    quantity=5
)

# Place orders
order1.place_order()
order2.place_order()

# Calculate total price with tax
order1.calculateprice()
order2.calculateprice()

# Cancel an order
order2.cancel_order()

# Try cancelling an order that wasn't placed
order3 = eorder(
    order_id=203,
    customer_name="lalith",
    customer_address="789 Oak Rd",
    customer_phoneno="555-9012",
    price=80,
    quantity=1
)
order3.cancel_order()  # This will log "Order was not placed yet"

# Update tax percentage
eorder.update_tax(10)

# Recalculate price after updating tax
order1.calculateprice()
order2.calculateprice()
