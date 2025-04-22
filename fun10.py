def place_order(customer_name, **order_details):
    print(f"Order Details for : ",customer_name)
    print("-" * 30)
    total = 0
    for item, price in order_details.items():
        print(f"{item:20}: ₹{price}")
        total += price
    print("-" * 30)
    print(f"{'Total Amount':20}: ₹{total}")
    print("Your food will arrive soon!\n")

# Placing food orders using keyword arguments
place_order("Krishna Yadav",
            Pizza=250,
            Burger=150,
            Pasta=200)

place_order("Sonal Rathore",
            Pasta=200,
            Burger=150,
            Juice=80)
