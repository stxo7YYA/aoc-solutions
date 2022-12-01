f = open('input', 'r')
calories = 0
top = []
for line in f.readlines():
    if line == '\n':
        top.append(calories)
        calories = 0
        continue
    calories += int(line)
top.sort()
print('Part One', max(top))
print('Part Two', sum(top[-3:]))
