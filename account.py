class Account: 
	def __init__ (self, name, balance, transactions):
		self.name = name
		self.balance = balance
		self.transactions = transactions
	
	def __str__(self) -> str:
		return "Name: {}, Balance: {}, Transactions: {}".format(self.name, self.balance, len(self.transactions))