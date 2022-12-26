from account import Account
from transaction import Transaction
from request import handle_request

# Gets all accounts for the given user access token and logs the Name, number of transations and Balance for them
def get_accounts() -> list:	
	accounts_response = handle_request("/accounts")
	accounts = []
	for val in accounts_response["data"] :
		id = val["id"]
		accountAttr = val["attributes"]
		name = accountAttr["displayName"]
		balance = accountAttr["balance"]["value"]

		transactions_response = handle_request("/accounts/{}/transactions".format(id))
		transactions = []
		for t in transactions_response["data"] :
			attr = t["attributes"]
			transaction = Transaction(attr["amount"]["value"], attr["status"], attr["createdAt"], attr["message"])
			transactions.append(transaction)
		accounts.append(Account(name, balance, transactions))
	return accounts

