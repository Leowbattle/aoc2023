lines = open("input").readlines()

def func(line):
	digits = list(filter(str.isdigit, line))
	return 10 * (int(digits[0])) + int(digits[-1])

print(sum(map(func, lines)))