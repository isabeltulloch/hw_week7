from person import Person
from customer import Customer
from employee import Employee

# GETTER - RETURN VALUE
# SETTER - SET INPUT

Ada_Thorne = Person("Ada", "Thorne")
print(Ada_Thorne)
Thomas_Shelby = Customer("Thomas", "Shelby")
print(Thomas_Shelby)
Arthur_Shelby = Employee("Arthur", "Shelby", "Control", "Manager")
print(Arthur_Shelby)
# Thomas_Shelby.set_items_bought('apples', 'oranges', 'pears')
# print(Thomas_Shelby.get_items_bought())
# Thomas_Shelby.set_gender("male")
# print(Thomas_Shelby.get_gender())