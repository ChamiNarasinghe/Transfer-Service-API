# Transfer-Service-API
This is a simple RESTful API built with Flask for transferring funds between accounts. The API allows you to create accounts, transfer funds between them, and check the balance of individual accounts.

## Features :
Create Account: Initialize accounts with a specified balance.

Transfer Funds: Transfer a specified amount from one account to another.

Check Balance: Retrieve the balance of a specific account.

## Project Structure :
1.app.py: The main Flask application that defines the API endpoints.
2.models.py: Contains the Account and Transaction classes used to represent the core data models.
3.services.py: Implements the TransferService class, handling the business logic for account creation, fund transfer, and balance retrieval.

## API Endpoints :

1.Transfer Funds

Endpoint: /transfer
Method: POST

2. Check Account Balance

Endpoint: /balance/<account_number>
Method: GET

## Postman Screenshot:

![Screenshot (269)](https://github.com/user-attachments/assets/969d31ab-d60a-474b-abec-e7e3819364ac)

![Screenshot (264)](https://github.com/user-attachments/assets/27d7b95c-2355-4faf-b72e-33d9e72c2525)
![Screenshot (265)](https://github.com/user-attachments/assets/7b56aec0-8dc5-4d6a-b971-cbe63056b675)
![Screenshot (266)](https://github.com/user-attachments/assets/31dc8acb-3395-4bc3-a286-afe02beb8031)
![Screenshot (267)](https://github.com/user-attachments/assets/0a94f8c3-5aca-420d-af24-49e1865fd7c2)
![Screenshot (268)](https://github.com/user-attachments/assets/02eb08d4-af2b-42a8-a6f6-38715067909b)
