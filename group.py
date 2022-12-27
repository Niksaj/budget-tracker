def group_transactions(transactions) :
	groupedTransactions = dict()
	for transaction in transactions :
		dateVal = str.split(transaction.created_at, "T")[0]
		if (dateVal in groupedTransactions) :
			groupedTransactions[dateVal] = groupedTransactions[dateVal] + float(transaction.amount)
		else :
			groupedTransactions[dateVal] = float(transaction.amount)

	return groupedTransactions

def group_accounts(accounts) :
	groupedAccounts = dict()
	for account in accounts :
		groupedAccounts[account.name] = group_transactions(account.transactions)

	return groupedAccounts