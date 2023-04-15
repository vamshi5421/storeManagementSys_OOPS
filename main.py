import csv

class Item:

    pay_rate = 0.8 # Class Attribute, The pay rate after 20% discount
    all = [] # Class Attribute, List to keep track of all the items


    def __init__(self, name: str, price: float, quantity = 0): # quantity is optional, to assume a default value of 0
        
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal zero"

        # Assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity

        # Add the object to the list
        Item.all.append(self) 

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv") as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name = item["name"],
                price = float(item["price"]),
                quantity = int(item["quantity"])
            )

    def __repr__(self):
        return f"Item('{self.name},' {self.price}, {self.quantity})"


Item.instantiate_from_csv()

print(Item.all)

