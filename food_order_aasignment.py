class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None  
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = len(self.food_items) + 1
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                break

    def view_all_food_items(self):
        for food_item in self.food_items:
            print(f"Food ID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print("-------------------------")

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_new_order(self, food_ids):
        ordered_items = []
        for food_item in admin.food_items:
            if food_item.food_id in food_ids:
                ordered_items.append(food_item)
        self.orders.append(ordered_items)
        print("Order placed successfully")

    def view_order_history(self):
        if not self.orders:
            print("No order history found.")
            return
        for index, order in enumerate(self.orders, start=1):
            print(f"Order {index}:")
            for food_item in order:
                print(f"Name: {food_item.name}")
                print(f"Quantity: {food_item.quantity}")
                print(f"Price: {food_item.price}")
                print("-------------------------")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully")


# Creating an instance of Admin
admin = Admin()

# Adding food items
admin.add_food_item("Chicken", "4 pieces", 240, 0, 50)
admin.add_food_item("Burger", "1 piece", 320, 10, 100)
admin.add_food_item("Cake", "500gm", 900, 5, 20)

# Viewing all food items
admin.view_all_food_items()

# Creating an instance of User
user = User("Asif", "6737637736", "bhatasif7979.ab@example.com", "11 lane", "password")

# Placing a new order
user.place_new_order([2, 3])

# Viewing order history
user.view_order_history()

# Updating profile
user.update_profile("Menuu", "5667887765", "menuu@example.com", "456 lane", "newpassword")