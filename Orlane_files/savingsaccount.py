from account import Account

class SavingsAccount(Account):
    def __init__(self, first_name, last_name, initial_balance, interest_rate):
        super().__init__(first_name, last_name, initial_balance)
        self.interest_rate = interest_rate

    def __str__(self):
        savings_info = self.get_first_name() + " " + self.get_last_name()
        savings_info += "'s"
        return savings_info + " savings account has balance " + str(self.getbalance())

    def calculate_interest(self):
        return self.get_balance() * self.interest_rate