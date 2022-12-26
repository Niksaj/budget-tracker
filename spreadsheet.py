from constants import DATE_TIME_FORMAT, EXPORT_DIRECTORY
from datetime import datetime
import xlsxwriter

def write_accounts(accounts) :
	now = datetime.now();
	workbook = xlsxwriter.Workbook("{}Account Transactions_{}.xlsx".format(EXPORT_DIRECTORY, now.strftime(DATE_TIME_FORMAT)))
	for account in accounts :
		worksheet = workbook.add_worksheet("{} - {}".format(account.name, account.balance))
		for i, transaction in enumerate(account.transactions) :
			index = i + 1 #worksheet starts at 1, arrays start at 0
			worksheet.write("A{}".format(index), transaction.amount)
			worksheet.write("B{}".format(index), transaction.status)
			worksheet.write("C{}".format(index), transaction.created_at)
			worksheet.write("D{}".format(index), transaction.message)
	workbook.close()