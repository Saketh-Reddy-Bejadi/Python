import re
import openpyxl

class BloodBank:
    def __init__(self):
        self.donors = []
        self.buyers = []

    def add_donor(self, name, phone_number, email_id, aadhar_number):
        donor = {"name": name, "phone_number": phone_number, "email_id": email_id, "aadhar_number": aadhar_number}
        self.donors.append(donor)
        print("Donor added successfully.")

    def add_buyer(self, name, phone_number, email_id, aadhar_number):
        buyer = {"name": name, "phone_number": phone_number, "email_id": email_id, "aadhar_number": aadhar_number}
        self.buyers.append(buyer)
        print("Buyer added successfully.")

    def display_donors(self):
        print("Donors:")
        for donor in self.donors:
            print("Name:", donor["name"])
            print("Phone Number:", donor["phone_number"])
            print("Email ID:", donor["email_id"])
            print("Aadhar Number:", donor["aadhar_number"])
            print("-------------------------")

    def display_buyers(self):
        print("Buyers:")
        for buyer in self.buyers:
            print("Name:", buyer["name"])
            print("Phone Number:", buyer["phone_number"])
            print("Email ID:", buyer["email_id"])
            print("Aadhar Number:", buyer["aadhar_number"])
            print("-------------------------")

    def save_data_to_excel(self):
        workbook = openpyxl.Workbook()
        donor_sheet = workbook.active
        donor_sheet.title = "Donors"

        headers = ["Name", "Phone Number", "Email ID", "Aadhar Number"]
        donor_sheet.append(headers)

        for donor in self.donors:
            donor_sheet.append([donor["name"], donor["phone_number"], donor["email_id"], donor["aadhar_number"]])

        buyer_sheet = workbook.create_sheet(title="Buyers")
        buyer_sheet.append(headers)

        for buyer in self.buyers:
            buyer_sheet.append([buyer["name"], buyer["phone_number"], buyer["email_id"], buyer["aadhar_number"]])

        file_name = "blood_bank_data.xlsx"
        workbook.save(file_name)
        print(f"Data saved to {file_name}")

    def validate_email_domain(self, email_id):
        valid_domains = ["gmail.com", "outlook.com"]  # Add more valid domains here

        pattern = r"@([\w.-]+)"
        match = re.search(pattern, email_id)

        if match:
            domain = match.group(1)
            if domain in valid_domains:
                return True

        return False


blood_bank = BloodBank()

while True:
    print("Blood Bank Management System")
    print("1. Add Donor")
    print("2. Add Buyer")
    print("3. Display Donors")
    print("4. Display Buyers")
    print("5. Save Data to Excel")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter donor name: ")
        phone_number = input("Enter donor phone number: ")
        email_id = input("Enter donor email ID: ")
        aadhar_number = input("Enter donor Aadhar number: ")

        if len(aadhar_number) == 12 and phone_number.isdigit() and len(phone_number) == 10 and blood_bank.validate_email_domain(email_id):
            blood_bank.add_donor(name, phone_number, email_id, aadhar_number)
        else:
            print("Invalid Aadhar number, phone number, or email ID. Please try again.")

    elif choice == "2":
        name = input("Enter buyer name: ")
        phone_number = input("Enter buyer phone number: ")
        email_id = input("Enter buyer email ID: ")
        aadhar_number = input("Enter buyer Aadhar number: ")

        if len(aadhar_number) == 12 and phone_number.isdigit() and len(phone_number) == 10 and blood_bank.validate_email_domain(email_id):
            blood_bank.add_buyer(name, phone_number, email_id, aadhar_number)
        else:
            print("Invalid Aadhar number, phone number, or email ID. Please try again.")

    elif choice == "3":
        blood_bank.display_donors()

    elif choice == "4":
        blood_bank.display_buyers()

    elif choice == "5":
        blood_bank.save_data_to_excel()

    elif choice == "6":
        print("Thank you for using the Blood Bank Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
