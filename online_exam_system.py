import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class examsystem:
    pass_marks = 21

    def __init__(self, student_rollno, student_name, marks):
        self.student_rollno = student_rollno
        self.student_name = student_name
        self.marks = marks
        self.examstarted = False
        self.examfinished = False  # exam started and exam finished are initially False
        logging.info("Exam record created | Roll No: %s | Name: %s | Marks: %d",
                     self.student_rollno, self.student_name, self.marks)

    # object method for start exam
    def startexam(self):
        self.examstarted = True
        logging.info("Exam started for Roll No: %s", self.student_rollno)

    # object method for submit exam
    def submitexam(self):
        self.examfinished = True
        logging.info("Exam submitted for Roll No: %s", self.student_rollno)

    # object method for calculating score
    def calculate_score(self):
        if self.marks > examsystem.pass_marks:
            logging.info("Result for Roll No %s: Passed", self.student_rollno)
        else:
            logging.info("Result for Roll No %s: Failed", self.student_rollno)

    # class method
    @classmethod
    def update_passmarks(cls, new_passmarks):
        cls.pass_marks = new_passmarks
        logging.info("Updated pass marks: %d", cls.pass_marks)
# Example usage of examsystem

# Create exam records for students
student1 = examsystem(student_rollno=101, student_name="Alice", marks=25)
student2 = examsystem(student_rollno=102, student_name="Bob", marks=18)

# Start exams
student1.startexam()
student2.startexam()

# Submit exams
student1.submitexam()
student2.submitexam()

# Calculate scores
student1.calculate_score()
student2.calculate_score()

# Update pass marks
examsystem.update_passmarks(20)

# Recalculate scores after updating pass marks
student1.calculate_score()
student2.calculate_score()
