import sys, re

for line in sys.stdin:
	line = line.rstrip()
	print(re.sub('human', 'computer', line))