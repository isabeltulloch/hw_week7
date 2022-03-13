# Class Employee - subclass of Person

# import Superclass
from person import Person

# for a subclass, the superclass name is in brackets
class Employee(Person):

    # constructor
    def __init__(self, first, last, company, city):
        super(Employee, self).__init__(first, last)
        # self.__first = first
        self.__company = company
        self.__city = city
        self.__company_location = company + ' is in ' + city

    # getters
    # get - company
    def get_company(self):
        return self.__company

    # get - city
    def get_city(self):
        return self.__city


    # setters
    # set - company
    def set_company(self, company):
        self.__company = company

    # set - city
    def set_city(self, city):
        self.__city = city

    # function for company location
    def company_location(self):
        return self.__company + ' is in ' + self.__city

    # Polymorphism
    def __str__(self):
        return "I am an employee. My name is: " + self.__first