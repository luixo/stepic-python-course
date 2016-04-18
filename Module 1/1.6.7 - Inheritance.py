classes = {}
for i in range(int(input())):
	data = input().split(' : ')
	if (len(data) == 1):
		data.append("")
	classes[data[0]] = data[1].split()
	for j in classes[data[0]]:
		if j not in classes:
			classes[j] = []

#print(classes)
def is_parent(child, parent):
	#print('checking if ' + child + ' is a child of ' + parent)
	if parent in classes[child] or child == parent:
		return True
	if len(classes[child]):
		return any(map(lambda x: is_parent(x, parent), classes[child]))

for i in range(int(input())):
	data = input().split()
	print("Yes" if is_parent(data[1], data[0]) else "No")