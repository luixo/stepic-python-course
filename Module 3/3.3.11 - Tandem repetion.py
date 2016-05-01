import sys, re

for line in sys.stdin:
	line = line.rstrip()
	if len(re.findall(r"\b(.+)\1\b", line)) > 0:
		print(line)