from accounts import get_accounts
from spreadsheet import write_accounts
from group import group_accounts
from validation import validate_key

def main() :
	validate_key()
	accounts = get_accounts()
	groupedAccounts = group_accounts(accounts)
	write_accounts(groupedAccounts)

if __name__ == "__main__" :
	main()