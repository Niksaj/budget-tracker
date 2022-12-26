class Transaction: 
	def __init__(self, amount, status, created_at, message):
		self.amount = amount
		self.status = status
		self.created_at = created_at
		self.message = message