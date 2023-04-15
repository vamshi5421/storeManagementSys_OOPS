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
    
    def __repr__(self):
        return f"Item('{self.name},' {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5) 
item2 = Item("Laptop", 1000, 3)

item1.has_discount = True 
# name price and quantity are attributes of the object, 
# has_discount is also an attribute of the object... but it is not defined in the class, 
# which means it is a dynamic attribute and can be added to the object at any time

# print(item1.calculate_total_price()) # object is passed as an argument to the method, self is the object
# print(item2.calculate_total_price())

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# print(item3.calculate_total_price) # which should be 3000 


# print(Item.__dict__) # returns a dictionary of all the Class attributes.
# print(item1.__dict__) # returns a dictionary of all the Instance attributes.

item1.apply_discount()
print(item1.price) # 80.0

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price) # 800.0, the pay_rate of the object is 0.7, 
# which is different from the class attribute, bcoz earlier we used Item.pay_rate = 0.8, but now we used item2.pay_rate = 0.7, 
# so the class attribute is not changed, but the object attribute is changed

# Item.pay_rate  =>  self.pay_rate .....


print(Item.all) # __repr__ is called, which returns a string representation of the object


