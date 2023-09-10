# class Complaint:    
#     def __init__(self, complaint_id, customer_name, complaint_text):        
#         self.complaint_id = complaint_id        
#         self.customer_name = customer_name        
#         self.complaint_text = complaint_text        
#         self.status = "Open"
# class ComplaintSystem:    
#     def _init_(self):        
#         self.complaints = []    
#     def add_complaint(self, complaint_id, customer_name, complaint_text):        
#         complaint = Complaint(complaint_id, customer_name, complaint_text)
#         self.complaints.append(complaint)    
#     def get_complaint_by_id(self, complaint_id):        
#         for complaint in self.complaints:         
#             if complaint.complaint_id == complaint_id:            
#                 return complaint        
#         return None   
#     def update_complaint_status(self, complaint_id, new_status):      
#         complaint = self.get_complaint_by_id(complaint_id)    
#         if complaint:  
#             complaint.status = new_status            
#             print("Complaint status updated successfully.")
#         else:            
#             print("Complaint not found.")    
#     def display_all_complaints(self):       
#         if self.complaints:    
#             for complaint in self.complaints:               
#                 print(f"Complaint ID: {complaint.complaint_id}")             
#                 print(f"Customer Name: {complaint.customer_name}")            
#                 print(f"Complaint Text: {complaint.complaint_text}")            
#                 print(f"Status: {complaint.status}")      
#                 print("-----------------------------")     
#         else:          
#             print("No complaints found.")
# print("Consumer Complaint System")
# print("-------------------------")  
# print("1. Add Complaint") 
# print("2. Update Complaint Status") 
# print("3. Display All Complaints")
# print("4. Exit")
# print()
# complaint_system = ComplaintSystem()
# while True:    
#     choice = input("Enter your choice (1-4): ")  
#     print()  
#     if choice == "1":
#         complaint_id = input("Enter complaint ID: ")
#         customer_name = input("Enter customer name: ") 
#         complaint_text = input("Enter complaint text: ")
#         complaint_system.add_complaint(complaint_id, customer_name, complaint_text)
#         print("Complaint added successfully.")
#     elif choice == "2":
#         complaint_id = input("Enter complaint ID: ")
#         new_status = input("Enter new status: ")        
#         complaint_system.update_complaint_status(complaint_id, new_status)    
#     elif choice == "3":     
#         complaint_system.display_all_complaints()   
#     elif choice == "4":      
#         print("Exiting...")      
#         break    
#     else:        
#             print("Invalid choice. Please try again.")
#             print()


  


class Complaint:
    def __init__(self, complaint_id, customer_name, complaint_text):
        self.complaint_id = complaint_id
        self.customer_name = customer_name
        self.complaint_text = complaint_text
        self.status = "Open"

class ComplaintSystem:
    def __init__(self):  # Corrected constructor name
        self.complaints = []

    def add_complaint(self, complaint_id, customer_name, complaint_text):
        complaint = Complaint(complaint_id, customer_name, complaint_text)
        self.complaints.append(complaint)

    def get_complaint_by_id(self, complaint_id):
        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                return complaint
        return None

    def update_complaint_status(self, complaint_id, new_status):
        complaint = self.get_complaint_by_id(complaint_id)
        if complaint:
            complaint.status = new_status
            print("Complaint status updated successfully.")
        else:
            print("Complaint not found.")

    def display_all_complaints(self):
        if self.complaints:
            for complaint in self.complaints:
                print(f"Complaint ID: {complaint.complaint_id}")
                print(f"Customer Name: {complaint.customer_name}")
                print(f"Complaint Text: {complaint.complaint_text}")
                print(f"Status: {complaint.status}")
                print("-----------------------------")
        else:
            print("No complaints found.")

print("Consumer Complaint System")
print("-------------------------")
print("1. Add Complaint")
print("2. Update Complaint Status")
print("3. Display All Complaints")
print("4. Exit")
print()

complaint_system = ComplaintSystem()
while True:
    choice = input("Enter your choice (1-4): ")
    print()
    if choice == "1":
        complaint_id = input("Enter complaint ID: ")
        customer_name = input("Enter customer name: ")
        complaint_text = input("Enter complaint text: ")
        complaint_system.add_complaint(complaint_id, customer_name, complaint_text)
        print("Complaint added successfully.")
    elif choice == "2":
        complaint_id = input("Enter complaint ID: ")
        new_status = input("Enter new status: ")
        complaint_system.update_complaint_status(complaint_id, new_status)
    elif choice == "3":
        complaint_system.display_all_complaints()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        print()
