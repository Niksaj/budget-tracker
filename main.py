from accounts import get_accounts
from spreadsheet import write_accounts
from group import group_accounts

def main() :
	accounts = get_accounts()
	groupedAccounts = group_accounts(accounts)
	write_accounts(groupedAccounts)

if __name__ == "__main__" :
	main()