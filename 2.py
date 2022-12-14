f = open('input', 'r')
one = two = 0
for line in f.readlines():
    if line == '\n':
        break
    x, y = line.split()
    x = ord(x) - ord('A')
    y = ord(y) - ord('X')
    one += [7, 4, 1][(1 + x - y) % 3] + y
    two += [1 + (x - 1)%3, 4 + x, 7 + (x + 1)%3][y]
print('Part One', one)
print('Part Two', two)
