import sys, re

for line in sys.stdin:
	line = line.rstrip()
	if len(re.findall(r"cat", line)) > 1:
		print(line)