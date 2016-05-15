class Points:
	def __init__(self, k):
		self.size = k
		self.pts = []

	def add(self, *coords):
		self.pts.append(tuple(coords))
		#print('on add')
		#print(self.pts)

	def remove(self, *coords):
		res = self.pts
		for i, c in enumerate(coords):
			res = list(filter(lambda x: x[i] == c, res))
		if len(list(res)) > 0:
			self.pts.remove(list(res)[0])
		#print('on remove')
		#print(self.pts)

	def range_query(self, *coord_ranges):
		res = self.pts
		#print('the')
		#print(coord_ranges)
		for i, c in enumerate(coord_ranges):
			res = list(filter(lambda x: x[i] >= c[0] and x[i] <= c[1], res))
		#print('on range')
		#print(res)
		for point in res:
			yield point 
		
ps = Points(2)
ps.add(1, 1)
ps.add(3, 1)
print(list(ps.range_query((1, 3), (1, 1)))) # [(1, 1), (3, 1)]
ps.add(3, 1)
print(list(ps.range_query((2, 3), (1, 1)))) # [(3, 1), (3, 1)]
ps.remove(2, 1)
ps.remove(3, 1)
print(list(ps.range_query((1, 3), (1, 1)))) # [(1, 1), (3, 1)]