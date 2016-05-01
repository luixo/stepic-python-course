import csv, re

with open("crimes.csv") as file:
	list = [crime[5] for crime in filter(lambda x: re.match(r'.*2015', x[2]), csv.reader(file))]
	print(max(set(list), key=list.count))