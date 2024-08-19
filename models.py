class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class Transaction:
    def __init__(self, source_account, destination_account, amount):
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
