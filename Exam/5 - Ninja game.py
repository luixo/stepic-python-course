height, jump = map(int, input().split())
left = list(input())
right = list(input())
for i in range(1, jump + 1):
	if left[height - i] == '-':
		left[height - i] = 'o'
	if right[height - i] == '-':
		right[height - i] = 'o'
if jump < height:
	for i in range(jump + 1, height + 1):
		if not left[height - i] == 'X':
			if left[height - i + 1] == 'o' or right[height - i + jump] == 'o':
				left[height - i] = 'o'
				start = height - i + 1
				while not left[start] == 'X':
					if start == height - 1:
						break
					left[start] = 'o'
					start += 1
				
		if not right[height - i] == 'X':
			if right[height - i + 1] == 'o' or left[height - i + jump] == 'o':
				right[height - i] = 'o'
				start = height - i + 1
				while not right[start] == 'X':
					if start == height - 1:
						break
					right[start] = 'o'
					start += 1
if left[0] == 'o':
	print('YES')
else:
	print('NO')