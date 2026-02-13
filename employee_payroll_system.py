import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class payroll:
    hra_percentage = 20

    def __init__(self, emp_id, emp_name, empsal, leavedays):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.empsal = empsal
        self.leavedays = leavedays
        self.netsal = 0  # initially assuming salary is 0
        logging.info(
            "Employee created | ID: %s | Name: %s | Base Salary: %.2f",
            self.emp_id, self.emp_name, self.empsal
        )

    # object method for calculating salary
    def calculatesal(self):
        hra = (self.empsal * payroll.hra_percentage) / 100
        self.netsal = self.empsal + hra
        logging.info(
            "Net salary calculated | Employee ID: %s | Net Salary: %.2f",
            self.emp_id, self.netsal
        )

    def leavededuction(self):
        per_day_salary = self.empsal / 30
        deduction = per_day_salary * self.leavedays
        self.netsal -= deduction
        logging.info(
            "Leave deduction applied | Employee ID: %s | Net Salary After Deduction: %.2f",
            self.emp_id, self.netsal
        )

    def payslip(self):
        logging.info("Payslip generated | Employee ID: %s", self.emp_id)
        logging.info("Employee Name: %s", self.emp_name)
        logging.info("Employee Base Salary: %.2f", self.empsal)
        logging.info("Employee Net Salary: %.2f", self.netsal)

    # class method for updating hra percentage
    @classmethod
    def update_hra(cls, new_hra):
        cls.hra_percentage = new_hra
        logging.info("Updated HRA percentage: %d%%", cls.hra_percentage)



emp1 = payroll(emp_id=101, emp_name="Alice", empsal=50000, leavedays=2)
emp2 = payroll(emp_id=102, emp_name="Bob", empsal=40000, leavedays=4)

# Calculate salary with HRA
emp1.calculatesal()
emp2.calculatesal()

# Apply leave deductions
emp1.leavededuction()
emp2.leavededuction()

# Generate payslips
emp1.payslip()
emp2.payslip()

# Update HRA percentage
payroll.update_hra(25)

# Recalculate salary after HRA update
emp1.calculatesal()
emp1.leavededuction()
emp1.payslip()
