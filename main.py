import csv

class Item:

    pay_rate = 0.8 
    all = [] 


    def __init__(self, name: str, price: float, quantity = 0): 
        
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

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else :
            return False

    def __repr__(self):
        return f"Item('{self.name},' {self.price}, {self.quantity})"


Item.instantiate_from_csv()


# Inheriting from Item class
class Phone(Item):
    
    all = []

    def __init__(self, name: str, price: float, quantity = 0, broken_phone = 0): 
        
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal zero"
        assert broken_phone >= 0, f"Broken Phones {broken_phone} is not greater than or equal zero"
        # Assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity
        self.broken_phone = broken_phone

        # Add the object to the list
        Phone.all.append(self)




phone1 = Phone("samsungPhone", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("iphonePhone", 1200, 5, 1)
