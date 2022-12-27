from constants import DATE_TIME_FORMAT, EXPORT_DIRECTORY
from datetime import datetime
import xlsxwriter
import os

def setup_output() :
	if not os.path.exists(EXPORT_DIRECTORY) :
		os.makedirs(EXPORT_DIRECTORY)

def create_chart(workbook, worksheet, sheetName, length) :
	chart = workbook.add_chart({"type": "scatter"})
	chart.add_series({
		"values": "='{}'!$A$1:$A${}".format(sheetName, length),
		"categories": "='{}'!$B$1:$B${}".format(sheetName, length)
	})
	worksheet.insert_chart("I1", chart)

def write_accounts(accounts) :
	setup_output()

	# Create workbook
	now = datetime.now()
	workbook = xlsxwriter.Workbook("{}Account Transactions_{}.xlsx".format(EXPORT_DIRECTORY, now.strftime(DATE_TIME_FORMAT)))
	
	# setup formats
	money = workbook.add_format({"num_format": "$#.##0"})
	dateFormat = workbook.add_format({"num_format":"mm/dd/yyyy"})

	# Write each account to spreadsheet
	for name, transactions in accounts.items() :
		worksheet = workbook.add_worksheet(name)
		
		i = 0
		# Write each transaction 
		for date, value in transactions.items() :
			worksheet.write_number(i, 0, float(value), money)
			worksheet.write_datetime(i, 1, datetime.strptime(str.split(date, "+")[0], "%Y-%m-%d"), dateFormat)
			i += 1

		create_chart(workbook, worksheet, name, len(transactions))

	workbook.close()