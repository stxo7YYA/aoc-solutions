f = open('input', 'r')
n = [[0, 0] for _ in range(10)]
one, two = set(), set()
for line in f:
	if line == '\n': break
	m = line.split()
	d = m[0]
	for i in range(int(m[1])):
		match d:
			case 'U': n[0][0] -= 1
			case 'R': n[0][1] += 1
			case 'D': n[0][0] += 1
			case 'L': n[0][1] -= 1
		for j in range(1, 10):
			py, px = n[j - 1][0], n[j - 1][1]
			cy, cx = n[j][0], n[j][1]
			if not (abs(py - cy) <= 1 and abs(px - cx) <= 1):
				if py == cy or px == cx:
					if py < cy: n[j][0] -= 1
					if px > cx: n[j][1] += 1
					if py > cy: n[j][0] += 1
					if px < cx: n[j][1] -= 1
				else:
					if py < cy and px > cx:
						n[j][0] -= 1
						n[j][1] += 1
					if py > cy and px > cx:
						n[j][0] += 1
						n[j][1] += 1
					if py > cy and px < cx:
						n[j][0] += 1
						n[j][1] -= 1
					if py < cy and px < cx:
						n[j][0] -= 1
						n[j][1] -= 1
		one.add((n[1][0], n[1][1]))
		two.add((n[9][0], n[9][1]))
print('Part One', len(one))
print('Part Two', len(two))
