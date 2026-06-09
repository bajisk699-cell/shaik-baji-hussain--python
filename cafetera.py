class FoodItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
class Employee:
    def __init__(self, employee_id: str, name: str):
        self.employee_id = employee_id
        self.name = name
class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.ordered_items = []
    def add_food_item(self, food_item: FoodItem):
        self.ordered_items.append(food_item)
    def calculate_total(self) -> float:
        return sum(item.price for item in self.ordered_items)
class Cafeteria:
    def __init__(self):
        self.menu = []
    def add_food_item(self, food_item: FoodItem):
        self.menu.append(food_item)
    def display_menu(self):
        print("Available Menu:")
        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item.name} - ₹{item.price:.2f}")
    def place_order(self, employee: Employee, order_id: str, selected_indices: list) -> Order:
        order = Order(order_id)
        for index in selected_indices:
            if 1 <= index <= len(self.menu):
                order.add_food_item(self.menu[index - 1])
        return order
    def generate_bill(self, employee: Employee, order: Order):
        total_amount = order.calculate_total()
        print("=" * 50)
        print(" CORPORATE CAFETERIA BILL ")
        print("=" * 50)
        print(f"Employee ID : {employee.employee_id}")
        print(f"Employee Name : {employee.name}")
        print("-" * 50)
        print(f"{'Item':<35} {'Price'}")
        print("-" * 50)
        for item in order.ordered_items:
            print(f"{item.name:<35} ₹{item.price:.0f}")  
        print("-" * 50)
        print(f"Total Amount ₹{total_amount:.0f}")
        print("Payment Status PAID")
        print("=" * 50)
cafeteria = Cafeteria()
cafeteria.add_food_item(FoodItem("Coffee", 40))
cafeteria.add_food_item(FoodItem("Sandwich", 80))
cafeteria.add_food_item(FoodItem("Brownie", 60))
emp = Employee("E101", "Ryan")
customer_order = cafeteria.place_order(emp, "ORD001", [1, 2, 3])
cafeteria.generate_bill(emp, customer_order)
