# Class Customer - subclass of Person

# import Superclass
from person import Person

class Customer(Person):
    numCreated = 0

    def __init__(self, first, last, item, price):
        super().__init__(first, last)
        self.__item = item
        self.__price = price

    # getter
    def get_item(self):
        return self.__item

    # setters
    def set_item(self, item):
        self.__item = item

    # getter
    def get_price(self):
        return self.__price

    # setters
    def set_price(self, price):
        self.__price = price

    # functions
    def calculate_discount(self):
        return "Your purchase of " + self.__item + " has been reduced to " + str(self.__price * 0.90)