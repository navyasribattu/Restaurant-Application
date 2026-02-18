# Restaurant Application

def display_menu(menu):
    print("\n----- Restaurant Menu -----")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")
    print("----------------------------")


def take_order(menu):
    order = {}
    
    while True:
        item = input("Enter item name to order (or type 'done' to finish): ").title()
        
        if item.lower() == 'done':
            break
        
        if item in menu:
            try:
                quantity = int(input(f"Enter quantity for {item}: "))
                if quantity > 0:
                    order[item] = order.get(item, 0) + quantity
                    print(f"{item} added to your order.")
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Item not found in menu. Please choose again.")
    
    return order


def calculate_bill(order, menu):
    total = 0
    print("\n----- Order Summary -----")
    for item, quantity in order.items():
        price = menu[item]
        subtotal = price * quantity
        total += subtotal
        print(f"{item} x {quantity} = ₹{subtotal}")
    
    print("--------------------------")
    print(f"Total Bill: ₹{total}")
    return total


def main():
    menu = {
        "Pizza": 250,
        "Burger": 120,
        "Pasta": 180,
        "Sandwich": 100,
        "Coffee": 80,
        "Tea": 50
    }
    
    print("Welcome to Python Restaurant!")
    
    while True:
        print("\n1. View Menu")
        print("2. Place Order")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_menu(menu)
        
        elif choice == "2":
            display_menu(menu)
            order = take_order(menu)
            if order:
                calculate_bill(order, menu)
            else:
                print("No items ordered.")
        
        elif choice == "3":
            print("Thank you for visiting!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
