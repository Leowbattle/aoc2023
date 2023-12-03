from collections import defaultdict

s = [line.strip() for line in open("input").readlines()]

def issymbol(c):
	return c != '.' and not c.isdigit()

gears = defaultdict(list)

for i in range(len(s)):
	line = s[i]

	j = 0
	while j < len(line):
		if not line[j].isdigit():
			j += 1
			continue

		n = 0
		g = set()
		
		while j < len(line) and line[j].isdigit():
			for k in range(i - 1, i + 2):
				for l in range(j - 1, j + 2):
					if k >= 0 and k < len(s) and l >= 0 and l < len(line):
						if s[k][l] == '*':
							g.add((k, l))

			n = 10 * n + int(line[j])
			j += 1

		for ge in g:
			gears[ge].append(n)

		j += 1

total = 0

for g in gears.values():
	if len(g) == 2:
		total += g[0] * g[1]

print(total)