a = input()
b = input()
c = input()
if not b in a:
	print('0')
elif b in c:
	print('Impossible')
else:
	count = 0
	while b in a:
		count += 1
		a = a.replace(b, c)
	print(count)