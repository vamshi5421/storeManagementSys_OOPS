import csv

class Item:

    pay_rate = 0.8 
    all = [] 


    def __init__(self, name: str, price: float, quantity = 0): 
        
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal zero"

        # Assign to self object
        self.__name = name
        self.__price = price 
        self.quantity = quantity

        # Add the object to the list
        Item.all.append(self) 


    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_val):
        self.__price = self.__price + self.__price * increment_val

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception("The name of the item cannot be more than 10 characters")
        else :
            self.__name = name
    

    def calculate_total_price(self):
        return self.__price * self.quantity
    
   
    

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
        return f"{self.__class__.__name__}('{self.name},' {self.__price}, {self.quantity})"

    def __connect(self,smtp):
        pass

    def __prepare_body(self):
        return f"""
            Hello Customer,
            We have {self.name} {self.quantity} in stock.
            Regards,
            Vamshi
        """
    
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
        print("Email Sent")


