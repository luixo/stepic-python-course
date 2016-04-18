class Buffer:
	def __init__(self):
		self.buf = []
	def add(self, *a):
		for n in a:
			self.buf.append(n)
			if (len(self.buf) == 5):
				print(sum(self.buf))
				self.buf = []
	def get_current_part(self):
		return self.buf