from account import Account
from transaction import Transaction
from request import handle_request
from constants import BASE_URL

# Gets all transactions for a given account id
def get_transactions(id, transactions, url) -> list:
	transactions_response = handle_request(url)
	for t in transactions_response["data"] :
		attr = t["attributes"]
		transaction = Transaction(attr["amount"]["value"], attr["status"], attr["createdAt"], attr["message"])
		transactions.append(transaction)
	nextUrl = transactions_response["links"]["next"]
	if (nextUrl == None) :
		return transactions
	return get_transactions(id, transactions, nextUrl)

# Gets all accounts for the given user access token including transactions
def get_accounts() -> list:	
	accounts_response = handle_request(BASE_URL + "/accounts")
	accounts = []
	for val in accounts_response["data"] :
		id = val["id"]
		accountAttr = val["attributes"]
		name = accountAttr["displayName"]
		balance = accountAttr["balance"]["value"]

		accounts.append(Account(name, balance, get_transactions(id, [], "{}/accounts/{}/transactions?page[size]=100".format(BASE_URL, id))))
	return accounts
