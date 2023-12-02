games = open("input").readlines()

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
			if n > handfull[c]:
				handfull[c] = n
	return handfull["red"] * handfull["green"] * handfull["blue"]

print(sum(map(func, games)))