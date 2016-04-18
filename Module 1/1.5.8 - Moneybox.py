class MoneyBox:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = 0
	def can_add(self, v):
		return  self.current + v <= self.capacity
	def add(self, v):
		self.current += v