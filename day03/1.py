s = [line.strip() for line in open("input").readlines()]

def issymbol(c):
	return c != '.' and not c.isdigit()

total = 0

for i in range(len(s)):
	line = s[i]

	j = 0
	while j < len(line):
		n = 0
		ispart = False
		while j < len(line) and line[j].isdigit():
			for k in range(i - 1, i + 2):
				for l in range(j - 1, j + 2):
					if k >= 0 and k < len(s) and l >= 0 and l < len(line):
						if issymbol(s[k][l]):
							ispart = True

			n = 10 * n + int(line[j])
			j += 1

		if ispart:
			total += n

		j += 1

print(total)