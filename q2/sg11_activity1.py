class Patient:
  def __init__(self, name: str, bill_amount: float):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self) -> str:
    return self.__name

  def set_name(self, name: str):
    return self.__name = name

  def get_bill_amount(self) -> float:
    return self.__bill_amount

  def set_bill_amount(self, bill_amount: float):
    self.__bill_amount = bill_amount

  def calculate_bill(self) -> float:
    return self.__bill_amount

  def display_patient_type(self):
    print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):
    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


print("Hospital Billing System")
print("-------------------------")

patients = [
    Patient("Juan Dela Cruz", 15000.00),
    SeniorPatient("Maria Santos", 15000.00),
    PhilHealthPatient("Pedro Reyes", 15000.00),
]

for patient in patients:
    print(f"Patient Name:  {patient.get_name()}")
    patient.display_patient_type()
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}\n")
