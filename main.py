from phone import Phone
from keyboard import Keyboard


item1 = Phone("MyPhone", 1000, 1) #get pay_rate from Item class
item2 = Keyboard("MyKeyboard", 1000, 1) #get pay_rate from Keyboard class

item1.apply_discount()
item2.apply_discount()

print(item1.price)
print(item2.price)