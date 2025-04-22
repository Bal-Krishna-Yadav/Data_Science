class ShoppingCart:
    TAX_RATE = 0.08  # 8% tax

    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity, discount=0):
        """Add an item to the shopping cart."""
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity,
            'discount': discount
        })

    def process_order(self):
        """Calculate the total cost of the order including tax."""
        
        def apply_discount(price, discount):
            """Apply discount to the price."""
            return price * (1 - discount)

        def calculate_subtotal():
            """Calculate the subtotal of the items in the cart."""
            subtotal = 0
            for item in self.items:
                final_price = apply_discount(item['price'], item['discount'])
                subtotal += final_price * item['quantity']
                print(f"{item['name']}: {final_price:.2f} x {item['quantity']} = {final_price * item['quantity']:.2f}")
            return subtotal

        def add_tax(amount):
            """Add tax to the subtotal."""
            return amount * (1 + self.TAX_RATE)

        subtotal = calculate_subtotal()
        total_with_tax = add_tax(subtotal)

        print(f"Subtotal: {subtotal:.2f}")
        print(f"Total with tax: {total_with_tax:.2f}")
        return total_with_tax

# Example usage
cart = ShoppingCart()
cart.add_item("Laptop", 1000, 1, discount=0.1)  # 10% discount
cart.add_item("Mouse", 50, 2)                    # No discount
cart.add_item("Keyboard", 80, 1, discount=0.05)  # 5% discount

cart.process_order()