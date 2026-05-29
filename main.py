# ============================================
# PHARMACEUTICAL CARE APP (Basic Version)
# Python Console Application
# ============================================

# Patient Database
patients = []

# Function: Add Patient
def add_patient():
    print("\n--- Add New Patient ---")

    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")
    medicine = input("Enter Medicine Name: ")
    dosage = input("Enter Dosage: ")

    patient = {
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Medicine": medicine,
        "Dosage": dosage
    }

    patients.append(patient)

    print("\nPatient Added Successfully!")

# Function: View Patients
def view_patients():
    print("\n--- Patient Records ---")

    if len(patients) == 0:
        print("No patient records found.")
        return

    for i, patient in enumerate(patients):
        print(f"\nPatient #{i+1}")
        print("Name:", patient["Name"])
        print("Age:", patient["Age"])
        print("Disease:", patient["Disease"])
        print("Medicine:", patient["Medicine"])
        print("Dosage:", patient["Dosage"])

# Function: Search Patient
def search_patient():
    print("\n--- Search Patient ---")

    search_name = input("Enter Patient Name: ")

    found = False

    for patient in patients:
        if patient["Name"].lower() == search_name.lower():
            print("\nPatient Found!")
            print("Name:", patient["Name"])
            print("Age:", patient["Age"])
            print("Disease:", patient["Disease"])
            print("Medicine:", patient["Medicine"])
            print("Dosage:", patient["Dosage"])
            found = True

    if not found:
        print("Patient not found.")

# Function: Medicine Reminder
def medicine_reminder():
    print("\n--- Medicine Reminder ---")

    medicine = input("Enter Medicine Name: ")
    time = input("Enter Reminder Time: ")

    print(f"\nReminder Set!")
    print(f"Take {medicine} at {time}")

# Main Program
while True:

    print("\n================================")
    print(" PHARMACEUTICAL CARE SYSTEM ")
    print("================================")

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Medicine Reminder")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        medicine_reminder()

    elif choice == "5":
        print("\nExiting Program...")
        break

    else:
        print("\nInvalid Choice!")