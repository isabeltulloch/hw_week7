# Person class - this is the superclass for the Employee and Customer subclasses

class Person:

    # constructor
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    # functions
    def fullname(self):
        return self.__first + ' ' + self.__last

    # getter
    def get_person_fullname(self):
        return self.__fullname()

    # setter
    def set_full_name(self, first, last):
        self.__fullname = first + ' ' + last

    # polymorphism
    def __str__(self):
        return "I am a person. My name is: " + self.__first