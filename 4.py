f = open('input', 'r')
one = two = 0
for line in [*f][:-1]:
    (a, b), (x, y) = [[int(x) for x in x.split('-')] for x in line.split(',')]
    if x <= a and y >= b or a <= x and b >= y:
        one += 1
    if a >= x and a <= y or x >= a and x <= b:
        two += 1
print('Part One', one)
print('Part Two', two)
