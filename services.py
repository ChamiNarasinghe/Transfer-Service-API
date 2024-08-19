from models import Account, Transaction

class TransferService:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def create_account(self, account_number, balance):
        self.accounts[account_number] = Account(account_number, balance)

    def transfer(self, source_account_number, destination_account_number, amount):
        if source_account_number not in self.accounts:
            return "Source account does not exist", 400

        if destination_account_number not in self.accounts:
            return "Destination account does not exist", 400

        source_account = self.accounts[source_account_number]
        destination_account = self.accounts[destination_account_number]

        if source_account.balance < amount:
            return "Insufficient funds", 400

        source_account.balance -= amount
        destination_account.balance += amount

        transaction = Transaction(source_account_number, destination_account_number, amount)
        self.transactions.append(transaction)

        return "Transfer successful", 200

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            return "Account does not exist", 400
        return self.accounts[account_number].balance, 200
