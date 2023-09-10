Menu = {
    "1": {"item": "Biryani", "price": 200},
    "2": {"item": "Sandwich", "price": 20},
    "3": {"item": "Cool drink", "price": 90},
    "4": {"item": "Pizza", "price": 237},
    "5": {"item": "Ice Cream(Butter scotch)", "price": 600}
}

Cart = {}

def display_menu():
    print("Menu:")
    print("------")
    for item_id, item in Menu.items():
        print(f"{item_id}. {item['item']}: Rs {item['price']}")
    print()

def place_order():
    display_menu()
    while True:
        item_id = input("Enter the item ID (or 'q' to quit): ")
        if item_id == 'q':
            break
        elif item_id not in Menu:
            print("Invalid item ID. Please try again.")
            continue
        quantity = int(input("Enter the quantity: "))
        item = Menu[item_id]
        if item_id in Cart:
            Cart[item_id]["quantity"] += quantity
        else:
            Cart[item_id] = {
                "item": item["item"],
                "price": item["price"],
                "quantity": quantity
            }
        print(f"{item['item']} (x{quantity}) added to the cart.")

def update_item():
    item_id = input("Enter the item ID to update: ")
    if item_id not in Cart:
        print("Item not found in the cart.")
        return
    quantity = int(input("Enter the new quantity: "))
    Cart[item_id]["quantity"] = quantity
    print("Item quantity updated.")

def delete_item():
    item_id = input("Enter the item ID to delete: ")
    if item_id not in Cart:
        print("Item not found in the cart.")
        return
    del Cart[item_id]
    print("Item deleted from the cart.")

def generate_bill():
    print("Bill:")
    print("------")
    total = 0
    for item_id, item in Cart.items():
        item_total = item["price"] * item["quantity"]
        print(f"{item['item']} (x{item['quantity']}): Rs {item_total}")
        total += item_total
    print("------")
    print(f"Total: Rs {total}")

def thank_you_message():
    print("Thank you for visiting! Please come again.")

while True:
    print("Food Ordering System")
    print("--------------------")
    print("1. Place Order")
    print("2. Update Item Quantity")
    print("3. Delete Item")
    print("4. Generate Bill")
    print("5. Exit")
    choice = input("Enter your choice: ")
    print()
    
    if choice == '1':
        place_order()
    elif choice == '2':
        update_item()
    elif choice == '3':
        delete_item()
    elif choice == '4':
        generate_bill()
    elif choice == '5':
        thank_you_message()
        break
    else:
        print("Invalid choice. Please try again.")
    print()