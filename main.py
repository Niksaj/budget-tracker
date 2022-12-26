from accounts import get_accounts
from spreadsheet import write_accounts

def main() :
	accounts = get_accounts()
	write_accounts(accounts)
	

if __name__ == "__main__" :
	main()