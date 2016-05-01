import sys, re

for line in sys.stdin:
	line = line.rstrip()
	print(re.sub(r'\b[aA]+\b', 'argh', line, 1))