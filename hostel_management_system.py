import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class management:
    room_rent = 600

    def __init__(self, room_no, student_name, months):
        self.room_no = room_no
        self.student_name = student_name
        self.months = months
        self.allocated = False
        logging.info(
            "Student record created | Room No: %s | Student: %s | Months: %d",
            self.room_no, self.student_name, self.months
        )

    def allocateroom(self):
        self.allocated = True
        logging.info(
            "Room allocated | Room No: %s | Student: %s",
            self.room_no, self.student_name
        )

    def vacateroom(self):
        if self.allocated:
            self.allocated = False
            logging.info(
                "Room vacated | Room No: %s | Student: %s",
                self.room_no, self.student_name
            )
        else:
            logging.info(
                "Room was not allocated | Room No: %s",
                self.room_no
            )

    def monthlyfee(self):
        monthly_fee = self.months * management.room_rent
        logging.info(
            "Monthly fee calculated | Room No: %s | Fee: %d",
            self.room_no, monthly_fee
        )
        return monthly_fee

    @classmethod
    def updateroomrent(cls, newrent):
        cls.room_rent = newrent
        logging.info(
            "Room rent updated | New Rent: %d",
            cls.room_rent
        )
# Create student hostel records
student1 = management(room_no=101, student_name="Alice", months=6)
student2 = management(room_no=102, student_name="Bob", months=4)

# Allocate rooms
student1.allocateroom()
student2.allocateroom()

# Calculate monthly fees
student1.monthlyfee()
student2.monthlyfee()

# Vacate a room
student2.vacateroom()

# Try vacating a room that is already vacant
student2.vacateroom()

# Update room rent
management.updateroomrent(750)

# Recalculate fee after rent update
student1.monthlyfee()
