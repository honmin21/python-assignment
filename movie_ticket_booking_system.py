import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ticket:
    ticket_price = 500

    def __init__(self, ticket_id, movie_name, seats):
        self.ticket_id = ticket_id
        self.movie_name = movie_name
        self.seats = seats
        self.booked = False
        logging.info(
            "Ticket created | Ticket ID: %s | Movie: %s | Seats: %d",
            self.ticket_id, self.movie_name, self.seats
        )

    def bookseat(self):
        self.booked = True
        logging.info(
            "Seats booked | Movie: %s | Seats: %d",
            self.movie_name, self.seats
        )

    def calcelbooking(self):
        if self.booked:
            self.booked = False
            logging.info(
                "Booking cancelled | Movie: %s | Seats: %d",
                self.movie_name, self.seats
            )
        else:
            logging.info(
                "Ticket was not booked | Movie: %s",
                self.movie_name
            )

    def calculateticketprice(self):
        total_price = self.seats * ticket.ticket_price
        logging.info(
            "Ticket price calculated | Movie: %s | Total Price: %d",
            self.movie_name, total_price
        )
        return total_price

    @classmethod
    def updateticketprice(cls, newticket_price):
        cls.ticket_price = newticket_price
        logging.info(
            "Ticket price updated | New Price: %d",
            cls.ticket_price
        )
# Create ticket objects
ticket1 = ticket(ticket_id=501, movie_name="Inception", seats=3)
ticket2 = ticket(ticket_id=502, movie_name="Avatar", seats=2)

# Book seats
ticket1.bookseat()
ticket2.bookseat()

# Calculate ticket prices
ticket1.calculateticketprice()
ticket2.calculateticketprice()

# Cancel one booking
ticket2.calcelbooking()

# Try cancelling an unbooked ticket
ticket3 = ticket(ticket_id=503, movie_name="Interstellar", seats=4)
ticket3.calcelbooking()

# Update ticket price
ticket.updateticketprice(600)

# Recalculate price after update
ticket1.calculateticketprice()
