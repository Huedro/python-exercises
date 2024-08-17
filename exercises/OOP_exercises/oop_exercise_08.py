# Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price


class ShoppingCart:
    def __init__(self):
        self.shop_cart = []

    def __str__(self):
        return str(self.shop_cart)

    def add_item(self, item):
        self.shop_cart.append(item)

    def remove_item(self, item_name):
        for item in self.shop_cart:
            if item[1] == item_name:
                self.shop_cart.remove(item)

    def total_price(self):
        cost = 0
        for item in self.shop_cart:
            cost += item[0] * item[2]
        return cost

    def items_in_cart(self):
        for item in self.shop_cart:
            print(item[1], end=" ")


my_cart = ShoppingCart()
my_cart.add_item((2, "toddy", 5.50))
my_cart.add_item((1, "whey", 99.50))
my_cart.add_item((2, "leite", 7))
my_cart.items_in_cart()
print("\nTotal Price: R$", my_cart.total_price())

my_cart.remove_item("toddy")
my_cart.items_in_cart()
print("\nTotal Price: R$", my_cart.total_price())
