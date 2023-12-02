games = open("input").readlines()

MAX = {
	"red": 12,
	"green": 13,
	"blue": 14
}

def func(game: str):
	id, x = game.split(": ")
	id = int(id.split(" ")[1])
	x = [h.split(",") for h in x.split(";")]
	handfull = {"red": 0, "green": 0, "blue": 0}
	for h in x:
		for p in h:
			p = p.strip()
			n, c = p.split(" ")
			n = int(n)
			if n > MAX[c]:
				return 0
	return id

print(sum(map(func, games)))