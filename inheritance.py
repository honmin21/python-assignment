import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        logging.info(
            "Person created | Name: %s | Age: %d",
            self.name, self.age
        )

    def display_person(self):
        logging.info(
            "Person details | Name: %s | Age: %d",
            self.name, self.age
        )


class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        logging.info(
            "Student ID: %s",
            self.student_id
        )


class Teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        logging.info(
            "Teacher Subject: %s",
            self.subject
        )


class Academic:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

    def display_Academic(self):
        logging.info(
            "Academic details | Subject: %s | Marks: %d",
            self.subject, self.marks
        )


class sports:
    def __init__(self, sport_name, level):
        self.sport_name = sport_name
        self.level = level

    def display_sports(self):
        logging.info(
            "Sports details | Sport: %s | Level: %s",
            self.sport_name, self.level
        )


class allrounder(student, Academic, sports):
    def __init__(self, name, age, student_id, subject, marks, sport_name, level):
        student.__init__(self, name, age, student_id)
        Academic.__init__(self, subject, marks)
        sports.__init__(self, sport_name, level)

    def display_allrounder(self):
        logging.info("----- All Rounder Details -----")
        self.display_student()
        self.display_Academic()
        self.display_sports()


# -------------------------
# Example Usage

student1 = student("Yuuji Itadori", 16, "S101")
student1.display_student()

student2 = student("Ichigo Kurosaki", 16, "S102")
student2.display_student()

print("\n-----------------\n")

teacher1 = Teacher("Satoru Gojo", 28, "Jujutsu Cursed Techniques")
teacher1.display_teacher()

teacher2 = Teacher("Kisuke Urahara", 28, "Soul Techniques")
teacher2.display_teacher()

print("\n-----------------\n")

allrounder1 = allrounder(
    name="Gon Freecss",
    age=17,
    student_id="S201",
    subject="Nen",
    marks=92,
    sport_name="Rock Paper Scissors",
    level="State"
)
allrounder1.display_allrounder()

allrounder2 = allrounder(
    name="Kurapika Kurta",
    age=19,
    student_id="S202",
    subject="Chains",
    marks=100,
    sport_name="Scarlet Eyes Collecting",
    level="National"
)
allrounder2.display_allrounder()
