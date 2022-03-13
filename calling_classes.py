from person import Person
from employee import Employee
from customer import Customer

# instantiating a person
# person 1 full name
person_1 = Person('Isabel', 'Tulloch')
# person 2
person_2 = Person('Orlane', 'Doumbe')

# instantiating an employee
employee_1 = Employee('Isabel', 'Tulloch', 'Sky', 'Osterley')
print(employee_1.fullname())
print(employee_1.company_location())
employee_2 = Employee('Orlane', 'Doumbe', 'Makers', 'London')
print(employee_2.fullname())
print(employee_2.company_location())

# customer
customer_1 = Customer('Isabel', 'Tulloch', 'laptop', 1000)
print(customer_1.calculate_discount())

print(employee_1)
