from item import Item


item1 = Item("MyItem", 100, 1)

#setting an Attribute
item1.name = "otherItem"

#Getting an Attribute
item1.apply_increment(0.2)

print(item1.price)