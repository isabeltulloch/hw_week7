from person import Person


class Customer(Person):

    def __init__(self, first_name, last_name):
        super(Customer, self).__init__(first_name, last_name)
        self.items_bought = []

    def get_items_bought(self, *items):
        self.items_bought.append(items)

    def set_items_bought(self):
        separator = ", "
        return self.first_name + " " + self.last_name + " bought: " + separator.join(map(str,self.items_bought))
