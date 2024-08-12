class Shopping_Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        print(f"Added {item_name} to the cart.")
    
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                print(f"Removed {item_name} from the cart.")
                break
        else:
            print(f"Item {item_name} not found in the cart.")
    
    def calculate_total(self):
        total = sum(price for item_name, price in self.items)
        return total

cart = Shopping_Cart()
cart.add_item("Laptop", 1000)
cart.add_item("Headphones", 200)
cart.remove_item("Laptop")
print(f"Total price: {cart.calculate_total()}")
