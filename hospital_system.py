import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Patient:
    consultation_fee = 500

    def __init__(self, patient_id, patient_name, days_admitted):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.days_admitted = days_admitted
        self.is_admitted = True
        logging.info(
            "Patient created | ID: %s | Name: %s | Days Admitted: %d",
            self.patient_id, self.patient_name, self.days_admitted
        )

    # object method
    def admit_patient(self):
        self.is_admitted = True
        logging.info("Patient admitted | Name: %s", self.patient_name)

    # object method
    def discharge_patient(self):
        self.is_admitted = False
        logging.info("Patient discharged | Name: %s", self.patient_name)

    # object method
    def calculate_bill(self):
        charge_per_day = 1000
        total_bill = (self.days_admitted * charge_per_day) + Patient.consultation_fee
        logging.info(
            "Bill calculated | Name: %s | Total Bill: %d",
            self.patient_name, total_bill
        )

    # class method
    @classmethod
    def update_consultation_fee(cls, new_consultation_fee):
        cls.consultation_fee = new_consultation_fee
        logging.info(
            "Consultation fee updated | New Fee: %d",
            cls.consultation_fee
        )

p1 = Patient(101, "Srihita", 3)
p1.calculate_bill()
p1.discharge_patient()
Patient.update_consultation_fee(700)


    