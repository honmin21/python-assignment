import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class lbssystem:
    fine_perday = 5

    # constructor
    def __init__(self, book_id, book_name, dayslate):
        self.book_id = book_id
        self.book_name = book_name
        self.dayslate = dayslate
        self.bookissued = False
        logging.info(
            "Book created | ID: %s | Name: %s",
            self.book_id, self.book_name
        )

    # method to issue book
    def issuebook(self):
        self.bookissued = True
        logging.info("Book issued | Name: %s", self.book_name)

    # method to return book
    def returnbook(self):
        self.bookissued = False
        logging.info("Book returned | Name: %s", self.book_name)

    # method to calculate fine
    def fine_amount(self):
        if self.dayslate > 0:
            fine = self.dayslate * lbssystem.fine_perday
            logging.info(
                "Fine calculated | Name: %s | Fine: %d",
                self.book_name, fine
            )
            return fine
        return 0

    # class method to update fine per day
    @classmethod
    def new_fineperday(cls, newfine):
        cls.fine_perday = newfine
        logging.info(
            "Fine per day updated | New Fine: %d",
            cls.fine_perday
        )

# Create a book object
book1 = lbssystem(book_id=101, book_name="Python Programming", dayslate=3)

# Issue the book
book1.issuebook()

# Calculate fine
book1.fine_amount()

# Return the book
book1.returnbook()

# Update fine per day
lbssystem.new_fineperday(15)

# Recalculate fine
book1.fine_amount()
