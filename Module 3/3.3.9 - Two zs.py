import sys, re

for line in sys.stdin:
	line = line.rstrip()
	if len(re.findall(r"z.{3}z", line)) > 0:
		print(line)