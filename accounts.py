from account import Account
from transaction import Transaction
from request import handle_request
from constants import BASE_URL, PAGE_SIZE

# Gets all transactions for a given account id
def get_transactions(id, transactions, url) -> list:
	_, transactionsResponse = handle_request(url)
	for t in transactionsResponse["data"] :
		attr = t["attributes"]
		transaction = Transaction(attr["amount"]["value"], attr["status"], attr["createdAt"], attr["message"])
		transactions.append(transaction)
	nextUrl = transactionsResponse["links"]["next"]
	if (nextUrl == None) :
		return transactions
	return get_transactions(id, transactions, nextUrl)

# Gets all accounts for the given user access token including transactions
def get_accounts() -> list:
	_, accountsResponse = handle_request(BASE_URL + "/accounts")
	accounts = []
	for val in accountsResponse["data"] :
		id = val["id"]
		accountAttr = val["attributes"]
		name = accountAttr["displayName"]
		balance = accountAttr["balance"]["value"]

		transactions = get_transactions(id, [], "{}/accounts/{}/transactions?page[size]={}".format(BASE_URL, id, PAGE_SIZE))
		accounts.append(Account(name, balance, transactions))
	return accounts
