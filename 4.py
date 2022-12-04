f = open('input', 'r')
lines = [line.strip() for line in f][:-1]
one = 0
two = 0
for line in lines:
    a, b = line.split(',')
    a = [int(x) for x in a.split('-')]
    b = [int(x) for x in b.split('-')]
    if b[0] <= a[0] and b[1] >= a[1]\
    or a[0] <= b[0] and a[1] >= b[1]:
        one += 1
    if a[0] >= b[0] and a[0] <= b[1]\
    or b[0] >= a[0] and b[0] <= a[1]:
        two += 1
print('Part One', one)
print('Part Two', two)
