class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.prescriptions = []
    def add_prescription(self, medication, dosage, instructions):
        prescription = {
            'medication': medication,
            'dosage': dosage,
            'instructions': instructions}
        self.prescriptions.append(prescription)
    def __str__(self):
        info = f"\nPatient ID: {self.patient_id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nPrescriptions:\n"
        if not self.prescriptions:
            info += "  None\n"
        else:
            for idx, p in enumerate(self.prescriptions, start=1):
                info += f"  {idx}. {p['medication']} - {p['dosage']} - {p['instructions']}\n"
        return info
class EMRSystem:
    def __init__(self):
        self.patients = {}
    def add_patient(self, patient_id, name, age, gender):
        if patient_id in self.patients:
            print("Patient with this ID already exists.")
        else:
            self.patients[patient_id] = Patient(patient_id, name, age, gender)
            print("Patient added successfully.")
    def add_prescription(self, patient_id, medication, dosage, instructions):
        if patient_id not in self.patients:
            print("Patient not found.")
        else:
            self.patients[patient_id].add_prescription(medication, dosage, instructions)
            print("Prescription added.")
    def view_patient(self, patient_id):
        if patient_id not in self.patients:
            print("Patient not found.")
        else:
            print(self.patients[patient_id])
if __name__ == "__main__":
    emr = EMRSystem()
    emr.add_patient("P001", "John Doe", 45, "Male")
    emr.add_patient("P002", "Jane Smith", 29, "Female")
    emr.add_prescription("P001", "Paracetamol", "500mg", "Twice a day after meals")
    emr.add_prescription("P001", "Ibuprofen", "200mg", "Once a day")
    emr.add_prescription("P002", "Amoxicillin", "250mg", "Three times a day")
    emr.view_patient("P001")
    emr.view_patient("P002")
