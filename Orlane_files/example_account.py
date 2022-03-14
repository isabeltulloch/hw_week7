from account import Account, InsufficientFundsException

try:
    some_account = Account("Thomas", "Shelby", 500)
    some_account.withdraw(700)
except InsufficientFundsException:
    print("Error! Cannot withdraw this amount.")
except Exception:
    print("Error! There has been a problem.")
else:
    print("Withdrawal successful")
    print(some_account.get_balance())
finally:
    pass
# some_account.withdraw(300)
# print(some_account.get_balance())