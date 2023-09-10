import pandas as pd


class Medicine:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Pharmacy:
    def __init__(self):
        self.medicines = []

    def initialize_medicines(self):
        self.medicines.append(Medicine("Paracetamol", 100, 10))
        self.medicines.append(Medicine("Ibuprofen", 50, 15))
        self.medicines.append(Medicine("Aspirin", 75, 12))
        self.medicines.append(Medicine("Amoxicillin", 30, 20))
        self.medicines.append(Medicine("Lisinopril", 20, 18))
        self.medicines.append(Medicine("Metformin", 40, 25))
        self.medicines.append(Medicine("Atorvastatin", 60, 30))
        self.medicines.append(Medicine("Omeprazole", 35, 15))
        self.medicines.append(Medicine("Albuterol", 25, 22))
        self.medicines.append(Medicine("Insulin", 15, 50))

    def display_medicines(self):
        if not self.medicines:
            print("No medicines available.")
        else:
            data = []
            for medicine in self.medicines:
                data.append({"Name": medicine.name, "Quantity": medicine.quantity, "Price": medicine.price})
            df = pd.DataFrame(data)
            print(df)

    def add_medicine(self):
        name = input("Enter medicine name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        medicine = Medicine(name, quantity, price)
        self.medicines.append(medicine)
        print(f"Added {name} to the medicine list.")

    def delete_medicine(self):
        name = input("Enter medicine name to delete: ")
        for medicine in self.medicines:
            if medicine.name == name:
                self.medicines.remove(medicine)
                print(f"Deleted {name} from the medicine list.")
                return
        print(f"{name} not found in the medicine list.")

    def update_quantity(self):
        name = input("Enter medicine name to update quantity: ")
        new_quantity = int(input("Enter new quantity: "))
        for medicine in self.medicines:
            if medicine.name == name:
                medicine.quantity = new_quantity
                print(f"Updated quantity for {name} to {new_quantity}.")
                return
        print(f"{name} not found in the medicine list.")

    def update_price(self):
        name = input("Enter medicine name to update price: ")
        new_price = float(input("Enter new price: "))
        for medicine in self.medicines:
            if medicine.name == name:
                medicine.price = new_price
                print(f"Updated price for {name} to {new_price}.")
                return
        print(f"{name} not found in the medicine list.")

    def buy_medicine(self):
        name = input("Enter customer name: ")
        phone_number = input("Enter customer phone number: ")
        print("\nSelect a medicine to buy:")
        self.display_medicines()
        medicine_name = input("Enter the name of the medicine to buy: ")
        quantity = int(input("Enter the quantity to buy: "))

        for medicine in self.medicines:
            if medicine.name == medicine_name:
                if medicine.quantity >= quantity:
                    medicine.quantity -= quantity
                    print(f"\nPurchase Details:")
                    print(f"Customer Name: {name}")
                    print(f"Phone Number: {phone_number}")
                    print(f"Medicine: {medicine.name}")
                    print(f"Quantity: {quantity}")
                    print(f"Total Price: {medicine.price * quantity}")
                    return
                else:
                    print(f"Insufficient quantity of {medicine.name} available.")
                    return

        print(f"Medicine {medicine_name} not found in the medicine list.")


# Example usage
pharmacy = Pharmacy()
pharmacy.initialize_medicines()

while True:
    print("\nE-Pharmacy Menu:")
    print("1. Display Medicines")
    print("2. Add Medicine")
    print("3. Delete Medicine")
    print("4. Update Quantity")
    print("5. Update Price")
    print("6. Buy Medicine")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        pharmacy.display_medicines()
    elif choice == "2":
        pharmacy.add_medicine()
    elif choice == "3":
        pharmacy.delete_medicine()
    elif choice == "4":
        pharmacy.update_quantity()
    elif choice == "5":
        pharmacy.update_price()
    elif choice == "6":
        pharmacy.buy_medicine()
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
