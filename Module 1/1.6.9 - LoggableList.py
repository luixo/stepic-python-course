class LoggableList(list, Loggable):
	def append(self, element):
		self.log(element)
		super(LoggableList, self).append(element)