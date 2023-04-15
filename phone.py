from item import Item

class Phone(Item):
    

    def __init__(self, name: str, price: float, quantity = 0, broken_phone = 0): 
        
        super().__init__(name, price, quantity)

        # Run Validations to the received arguments
        assert broken_phone >= 0, f"Broken Phones {broken_phone} is not greater than or equal zero"
        
        # Assign to self object
        self.broken_phone = broken_phone
