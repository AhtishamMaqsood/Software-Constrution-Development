class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product_name, price, quantity):
      
        item = {
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def calculate_total(self):

        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_item("Laptop", 67000, 3)
cart1.add_item("Mouse", 1700, 4)

cart2.add_item("Keyboard", 4000, 1)
cart2.add_item("Headphones", 2500, 4)

print("Cart 1 Items:", cart1.items)
print("Cart 1 Total:", cart1.calculate_total())

print("\nCart 2 Items:", cart2.items)
print("Cart 2 Total:", cart2.calculate_total())