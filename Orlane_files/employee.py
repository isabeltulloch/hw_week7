from person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, department, role):
        super().__init__(first_name, last_name)
        self.department = department
        self.role = role

    def get_department(self):
        return self.department

    def get_role(self):
        return self.role

    def __str__(self):
        return "I am a employee. My name is: " + self.first_name + " " + self.last_name