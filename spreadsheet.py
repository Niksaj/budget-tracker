from constants import DATE_TIME_FORMAT, EXPORT_DIRECTORY
from datetime import datetime
import xlsxwriter
import os

def create_chart(workbook, worksheet, sheetName) :
	chart = workbook.add_chart({"type": "line"})
	chart.add_series({"values": "='{}'!A:A".format(sheetName)})
	worksheet.insert_chart("F1", chart)

def write_accounts(accounts) :
	if not os.path.exists(EXPORT_DIRECTORY) :
		os.makedirs(EXPORT_DIRECTORY)
	
	now = datetime.now();
	workbook = xlsxwriter.Workbook("{}Account Transactions_{}.xlsx".format(EXPORT_DIRECTORY, now.strftime(DATE_TIME_FORMAT)))
	for account in accounts :
		worksheetName = "{} - {}".format(account.name, account.balance);
		worksheet = workbook.add_worksheet(worksheetName)
		for i, transaction in enumerate(account.transactions) :
			worksheet.write(i, 0, float(transaction.amount))
			worksheet.write(i, 1, transaction.created_at)
			worksheet.write(i, 2, transaction.status)
			worksheet.write(i, 3, transaction.message)
		create_chart(workbook, worksheet, worksheetName)
	workbook.close()