import pandas as pd

stock = {
    'sneakers': [
        {'name': 'Nike Air Max', 'price': 100},
        {'name': 'Adidas Ultraboost', 'price': 120},
        {'name': 'Puma RS-X', 'price': 90},
        {'name': 'New Balance 574', 'price': 80},
        {'name': 'Reebok Classic', 'price': 70},
        {'name': 'Vans Old Skool', 'price': 60},
        {'name': 'Converse Chuck Taylor', 'price': 50},
        {'name': 'Under Armour HOVR', 'price': 110},
        {'name': 'Salomon Speedcross', 'price': 130},
        {'name': 'Mizuno Wave Rider', 'price': 95},
        {'name': 'Brooks Ghost', 'price': 100},
    ],
    'high heels': [
        {'name': 'Jimmy Choo', 'price': 300},
        {'name': 'Christian Louboutin', 'price': 500},
        {'name': 'Manolo Blahnik', 'price': 400},
        {'name': 'Gucci', 'price': 600},
        {'name': 'Prada', 'price': 550},
        {'name': 'Valentino', 'price': 450},
        {'name': 'Alexander McQueen', 'price': 350},
        {'name': 'Stuart Weitzman', 'price': 400},
        {'name': 'Versace', 'price': 500},
        {'name': 'Dolce & Gabbana', 'price': 550},
    ],
    'boots': [
        {'name': 'Timberland 6-Inch', 'price': 150},
        {'name': 'Dr. Martens 1460', 'price': 180},
        {'name': 'Sorel Caribou', 'price': 130},
        {'name': 'UGG Classic Short', 'price': 160},
        {'name': 'Caterpillar Second Shift', 'price': 110},
        {'name': 'Wolverine 1000 Mile', 'price': 250},
        {'name': 'Red Wing Iron Ranger', 'price': 300},
        {'name': 'Clarks Desert Boot', 'price': 120},
        {'name': 'Rocky S2V', 'price': 200},
        {'name': 'Danner Mountain Light', 'price': 280},
    ]
}

password = 'admin123'  # Predefined password

def display_stock_by_category():
    print("Available Categories:")
    for i, category in enumerate(stock, 1):
        print(f"{i}. {category}")
    
    choice = int(input("Enter the number of the category you want to display: "))
    categories = list(stock.keys())
    if 1 <= choice <= len(categories):
        category = categories[choice - 1]
        print(f"\nFootwear in {category}:")
        df = pd.DataFrame(stock[category])
        print(df)
    else:
        print("Invalid choice.")

# ... Rest of the code remains the same ...


def search_category(category):
    category = category.lower()
    if category in stock:
        print(f"\nFootwear in {category}:")
        df = pd.DataFrame(stock[category])
        print(df)
    else:
        print("Category not found.")

def add_footwear():
    category = input("Enter category: ").lower()
    if category in stock:
        name = input("Enter footwear name: ")
        price = float(input("Enter price: "))
        stock[category].append({'name': name, 'price': price})
        print("Footwear added successfully.")
    else:
        print("Category not found.")

def delete_footwear():
    category = input("Enter category: ").lower()
    if category in stock:
        name = input("Enter footwear name: ")
        for item in stock[category]:
            if item['name'] == name:
                stock[category].remove(item)
                print("Footwear deleted successfully.")
                return
        print("Footwear not found.")
    else:
        print("Category not found.")

def buy_footwear():
    category = input("Enter category: ").lower()
    if category in stock:
        print(f"\nFootwear in {category}:")
        for i, item in enumerate(stock[category], 1):
            print(f"{i}. Name: {item['name']}, Price: {item['price']}")
        choice = int(input("Enter the number of the footwear you want to buy (0 to cancel): "))
        if choice == 0 or choice > len(stock[category]):
            print("Invalid choice or cancelled.")
        else:
            chosen_item = stock[category][choice - 1]
            print(f"You bought {chosen_item['name']} for ${chosen_item['price']}. Thank you!")
            stock[category].remove(chosen_item)
    else:
        print("Category not found.")

# Main program loop
while True:
    print("\n---- Shoe Shop Management System ----")
    print("1. Display stock by category")
    print("2. Search category")
    print("3. Add footwear")
    print("4. Delete footwear")
    print("5. Buy footwear")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_stock_by_category()
    elif choice == '2':
        category = input("Enter category: ")
        search_category(category)
    elif choice == '3':
        add_footwear()
    elif choice == '4':
        admin_password = input("Enter admin password: ")
        if admin_password == password:
            delete_footwear()
        else:
            print("Incorrect password. Access denied.")
    elif choice == '5':
        buy_footwear()
    elif choice == '0':
        break
    else:
        print("Invalid choice.")

print("Exiting the program. Goodbye!")
