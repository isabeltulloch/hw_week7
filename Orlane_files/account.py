class Account:

    number_of_accounts_created = 0

    def __init__(self, first_name, last_name, initial_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.__balance = initial_balance
        Account.number_of_accounts_created += 1

    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):

        if amount > self.__balance:
            raise InsufficientFundsException('Error! Can not withdraw more than the balance.')
        self.__balance -= amount


    def get_balance(self):
        return "Your balance is " + str(self.__balance)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return "The name on this account is: " + self.first_name + " " + self.last_name


class InsufficientFundsException(Exception):
    'Error! Can not withdraw more than the balance.'
    pass