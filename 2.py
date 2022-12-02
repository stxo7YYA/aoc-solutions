def rot(n, r):
    n += r
    return 3 if not n else 1 if n > 3 else n

f = open('input', 'r')
one = 0
two = 0
for line in f.readlines():
    if line == '\n':
        break
    x, y = line.split()
    x = ord(x) - ord('A') + 1
    y = ord(y) - ord('X') + 1
    for i in range(-1, 2):
        if x == rot(y, i):
            one += [6, 3, 0][i + 1] + y
    match y:
        case 1:
            two += 0 + rot(x, -1)
        case 2:
            two += 3 + rot(x, 0)
        case 3:
            two += 6 + rot(x, +1)
print('part One', one)
print('Part Two', two)
