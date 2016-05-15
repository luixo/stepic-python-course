import os.path, csv, re

good = 0
for root, dirs, files in os.walk('./data'):
	for file in files:
		if file.endswith('.csv'):
			with open(os.path.join(root, file)) as file:
				reader = csv.reader(file)
				index = [i for i, item in enumerate(next(reader)) if re.search('pet', item, re.IGNORECASE)]
				if not len(index) == 0:
					cats = 0
					dogs = 0
					for item in reader:
						if re.search('cat', item[index[0]], re.IGNORECASE):
							cats += 1
						if re.search('dog', item[index[0]], re.IGNORECASE):
							dogs += 1
					if cats < dogs:
						good += 1
print(good)