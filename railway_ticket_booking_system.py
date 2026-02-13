import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class rticket:
    base_fare = 300

    def __init__(self, ticket_id, passenger_name, distance):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.distance = distance
        self.isbooked = False
        self.iscancelled = False
        logging.info(
            "Ticket created | Ticket ID: %s | Passenger: %s | Distance: %d km",
            self.ticket_id, self.passenger_name, self.distance
        )

    # object method for booking ticket
    def bookticket(self):
        self.isbooked = True
        self.iscancelled = False
        logging.info(
            "Ticket booked successfully | Ticket ID: %s | Passenger: %s",
            self.ticket_id, self.passenger_name
        )

    def calcellticket(self):
        if self.isbooked:
            self.iscancelled = True
            logging.info(
                "Ticket cancelled | Ticket ID: %s",
                self.ticket_id
            )
        else:
            logging.info(
                "Ticket was not booked | Ticket ID: %s",
                self.ticket_id
            )

    def calculate_fair(self):
        fare = rticket.base_fare + (self.distance * 5)  # 5 is fare per kilometer
        logging.info(
            "Fare calculated | Ticket ID: %s | Total Fare: %.2f",
            self.ticket_id, fare
        )
        return fare

    # class method
    @classmethod
    def newbasefare(cls, newbasefare):
        cls.base_fare = newbasefare
        logging.info(
            "Updated base fare: %d",
            cls.base_fare
        )
# Example usage of rticket class

# Create ticket objects
ticket1 = rticket(ticket_id=1001, passenger_name="srihita", distance=120)
ticket2 = rticket(ticket_id=1002, passenger_name="jahnavi", distance=45)


ticket1.bookticket()
ticket2.bookticket()

# Calculate fare
ticket1.calculate_fair()
ticket2.calculate_fair()

# Cancel one ticket
ticket2.calcellticket()

# Try cancelling a ticket that was not booked
ticket3 = rticket(ticket_id=1003, passenger_name="Charlie", distance=60)
ticket3.calcellticket()

# Update base fare
rticket.newbasefare(350)

# Recalculate fare after updating base fare
ticket1.calculate_fair()
ticket2.calculate_fair()
