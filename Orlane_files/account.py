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

        # if amount > self.__balance:
        #     raise Exception('Error! Can not withdraw more than the balance.')
        # self.__balance -= amount
        try:
            if amount < self.__balance:
                self.__balance -= amount
        except Exception:
            print("Error! Cannot withdraw this amount.")
        else:
            return "Your balance is now: " + str(self.__balance)
        finally:
            pass

    def get_balance(self):
        return self.__balance

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return "The name on this account is: " + self.first_name + " " + self.last_name