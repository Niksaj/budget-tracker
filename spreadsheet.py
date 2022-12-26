from constants import DATE_TIME_FORMAT, EXPORT_DIRECTORY
from datetime import datetime
import xlsxwriter
import os

def setup_output() :
	if not os.path.exists(EXPORT_DIRECTORY) :
		os.makedirs(EXPORT_DIRECTORY)

def create_chart(workbook, worksheet, sheetName) :
	chart = workbook.add_chart({"type": "line"})
	chart.add_series({"values": "='{}'!A:A".format(sheetName)})
	worksheet.insert_chart("F1", chart)

def write_accounts(accounts) :
	setup_output()

	now = datetime.now()
	workbook = xlsxwriter.Workbook("{}Account Transactions_{}.xlsx".format(EXPORT_DIRECTORY, now.strftime(DATE_TIME_FORMAT)))
	
	# setup formats
	money = workbook.add_format({"num_format": "$#,##0"})
	dateFormat = workbook.add_format({"num_format":"mm/dd/yyyy"})

	for account in accounts :
		worksheetName = "{} - {}".format(account.name, account.balance)
		worksheet = workbook.add_worksheet(worksheetName)
		for i, transaction in enumerate(account.transactions) :
			worksheet.write_number(i, 0, float(transaction.amount), money)
			worksheet.write_datetime(i, 1, datetime.strptime(str.split(transaction.created_at, "+")[0], "%Y-%m-%dT%H:%M:%S"), dateFormat)
			worksheet.write(i, 2, transaction.status)
			worksheet.write(i, 3, transaction.message)
		create_chart(workbook, worksheet, worksheetName)
	workbook.close()