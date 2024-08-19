from flask import Flask, request, jsonify
from services import TransferService

app = Flask(__name__)
transfer_service = TransferService()


@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    account_number = data.get('account_number')
    balance = data.get('balance')

    if not account_number or balance is None:
        return jsonify({'message': 'Account number and balance are required'}), 400

    transfer_service.create_account(account_number, balance)
    return jsonify({'message': 'Account created successfully'}), 201


@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.json
    source = data.get('source_account')
    destination = data.get('destination_account')
    amount = data.get('amount')

    message, status_code = transfer_service.transfer(source, destination, amount)
    return jsonify({'message': message}), status_code

@app.route('/balance/<account_number>', methods=['GET'])
def get_balance(account_number):
    balance, status_code = transfer_service.get_balance(account_number)
    return jsonify({'balance': balance}), status_code

if __name__ == '__main__':
    
    app.run(debug=True)

