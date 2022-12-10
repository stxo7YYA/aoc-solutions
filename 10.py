f = open('input', 'r')

register = 1
cycles = 0
one = 0
two = ''

def a():
    global cycles, one, two
    cycles += 1
    if cycles in (20, 60, 100, 140, 180, 220):
        one += register * cycles
    two += '#' if abs(register - (cycles - 1) % 40) <= 1 else '.'

for line in f:
    if line == '\n':
        break
    operation = line.split()
    if operation[0] == 'noop':
        a()
    if operation[0] == 'addx':
        a()
        a()
        register += int(operation[1])

print('Part One', one)
print('Part Two:')
off = 0
for i in range(6):
    print(two[off:off + 40])
    off += 40
