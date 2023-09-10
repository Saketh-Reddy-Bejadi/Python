import pandas as pd

class Employee:
    def __init__(self, name, phone_number, email_id, account_number):
        self.name = name
        self.phone_number = phone_number
        self.email_id = email_id
        self.account_number = account_number

    def to_dict(self):
        return {
            "Name": self.name,
            "Phone Number": self.phone_number,
            "Email ID": self.email_id,
            "Account Number": self.account_number
        }


class PayrollManagementSystem:
    def __init__(self):
        self.employees = []
        self.payments = []
        self.data_file = "payroll_data.txt"

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                for line in file:
                    name, phone_number, email_id, account_number = line.strip().split(",")
                    employee = Employee(name, phone_number, email_id, account_number)
                    self.employees.append(employee)
        except FileNotFoundError:
            print("No data file found. Starting with an empty employee list.")

    def save_data(self):
        with open(self.data_file, "w") as file:
            for employee in self.employees:
                file.write(f"{employee.name},{employee.phone_number},{employee.email_id},{employee.account_number}\n")

    def add_employee(self):
        name = input("Enter the name of the employee: ")
        phone_number = input("Enter the phone number of the employee: ")
        email_id = input("Enter the email ID of the employee: ")
        account_number = input("Enter the account number of the employee: ")
        employee = Employee(name, phone_number, email_id, account_number)
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")
        self.save_data()

    def delete_employee(self):
        name = input("Enter the name of the employee to delete: ")
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print(f"Employee {employee.name} deleted successfully.")
                self.save_data()
                return
        print("Employee not found.")

    def update_employee_details(self):
        name = input("Enter the name of the employee to update details: ")
        for employee in self.employees:
            if employee.name == name:
                phone_number = input("Enter the new phone number (leave blank to skip): ")
                email_id = input("Enter the new email ID (leave blank to skip): ")
                account_number = input("Enter the new account number (leave blank to skip): ")
                if phone_number:
                    employee.phone_number = phone_number
                if email_id:
                    employee.email_id = email_id
                if account_number:
                    employee.account_number = account_number
                print(f"Employee {employee.name}'s details updated successfully.")
                self.save_data()
                return
        print("Employee not found.")

    def pay_salary(self):
        name = input("Enter the name of the employee to pay salary: ")
        for employee in self.employees:
            if employee.name == name:
                salary = input("Enter the salary amount: ")
                self.payments.append({"Employee Name": employee.name, "Salary": salary})
                print(f"Salary of {salary} paid to {employee.name}.")
                self.save_data()
                return
        print("Employee not found.")

    def display_employee_details(self):
        if self.employees:
            data = [employee.to_dict() for employee in self.employees]
            df = pd.DataFrame(data)
            print(df)
        else:
            print("No employees found.")

    def display_payment_details(self):
        if self.payments:
            df = pd.DataFrame(self.payments)
            print(df)
        else:
            print("No payment records found.")

    def display_menu(self):
        print("Payroll Management System Menu:")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee Details")
        print("4. Pay Salary")
        print("5. Display Employee Details")
        print("6. Display Payment Details")
        print("0. Exit")

    def run(self):
        self.load_data()
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.delete_employee()
            elif choice == "3":
                self.update_employee_details()
            elif choice == "4":
                self.pay_salary()
            elif choice == "5":
                self.display_employee_details()
            elif choice == "6":
                self.display_payment_details()
            elif choice == "0":
                print("Thank you for using the Payroll Management System!")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage
if __name__ == "__main__":
    system = PayrollManagementSystem()
    system.run()
