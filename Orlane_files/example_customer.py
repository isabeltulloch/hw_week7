from customer import Customer

Thomas_Shelby = Customer("Thomas", "Shelby")
print(Thomas_Shelby.get_name())
Thomas_Shelby.get_items_bought('apples', 'oranges', 'pears')
print(Thomas_Shelby.set_items_bought())
Thomas_Shelby.set_gender("male")
print(Thomas_Shelby.get_gender())