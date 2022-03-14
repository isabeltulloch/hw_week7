
class Person:
    def __init__(self, first_name, last_name):
        self.gender = None
        self.age = None
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return "This person's first name is: " + self.first_name

    def get_last_name(self):
        return "This person's last name is: " + self.last_name

    def get_name(self):
        return "This person is: " + self.first_name + " " + self.last_name

    def get_age(self, age):
        self.age = age

    def set_age(self):
        return "This person is age: " + self.age

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return "This person is a: " + self.gender

    def __str__(self):
        return "I am a person. My name is: " + self.first_name + " " + self.last_name