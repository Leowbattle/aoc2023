lines = open("input").readlines()

digits = {
	"zero": 0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
	"0": 0,
	"1": 1,
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9
}

def func(line: str):
	mina = 1000000
	maxb = -1
	da = None
	db = None

	for d in digits.keys():
		a = line.find(d)
		b = line.rfind(d)

		if a != -1 and a < mina:
			mina = a
			da = d
		if b != -1 and b > maxb:
			maxb = b
			db = d
	
	if da == None or db == None:
		print(line)
		return 0
	return 10 * digits[da] + digits[db]

print(sum(map(func, lines)))