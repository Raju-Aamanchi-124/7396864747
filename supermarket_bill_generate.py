name = input("Enter your Name: ")

# Items list with prices
items_list = '''
Rice       Rs 10/kg
Sugar      Rs 8/kg
Oil        Rs 30/liter
Salt       Rs 25/kg
Paneer     Rs 40/kg
Maggie     Rs 12/pack
Boost      Rs 200/bottle
'''

# Item prices dictionary
items = {
    'rice': 10,
    'sugar': 8,
    'oil': 30,
    'salt': 25,
    'paneer': 40,
    'maggie': 12,
    'boost': 200
}

# Declaration
total_price = 0
price_list = []
item_list = []
quantity_list = []
item_price_list = []

# Main menu
while True:
    option = input("\nPress 1 to view the list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping!")
        break
    elif option == '1':
        print("\nAvailable Items:")
        print(items_list)

        while True:
            buy_option = input("Press 1 to buy or 2 to return to main menu: ")
            if buy_option == '2':
                break
            elif buy_option == '1':
                item = input("Enter item name: ").lower()

                if item in items:
                    while True:
                        quantity_input = input("Enter quantity: ")
                        if quantity_input.isdigit():
                            quantity = int(quantity_input)
                            break
                        else:
                            print("❌ Please enter a valid number.")

                    price = quantity * items[item]
                    total_price += price

                    # Store data
                    price_list.append((item, quantity, items[item], price))
                    item_list.append(item)
                    quantity_list.append(quantity)
                    item_price_list.append(price)
                else:
                    print("❌ Item not available. Please choose from the list.")

        # Billing section
        if total_price > 0:
            tax = total_price * 0.05
            final_amount = total_price + tax

            print("\n" + "=" * 80)
            print(f"{'ABCD Supermarket':^80}")
            print(f"{'Hyderabad':^80}")
            print(f"Customer Name: {name}")
            print("-" * 80)
            print(f"{'S.No':<6}{'Item':<15}{'Quantity':<15}{'Unit Price':<15}{'Total Price':<15}")
            print("-" * 80)

            for i, (item, qty, unit_price, total) in enumerate(price_list, 1):
                print(f"{i:<6}{item:<15}{qty:<15}{unit_price:<15}{total:<15}")

            print("-" * 80)
            print(f"{'Total Amount':<60} Rs {total_price:.2f}")
            print(f"{'Tax (12%)':<60} Rs {tax:.2f}")
            print(f"{'Final Amount':<60} Rs {final_amount:.2f}")
            print("=" * 80)
            print(f"{'Thank you & Visit Again!':^80}")
            print("=" * 80)
