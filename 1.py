f = open('input', 'r')
maximum = 0
calories = 0
top = []
for line in f.readlines():
    if line == '\n':
        maximum = max(maximum, calories)
        top.append(calories)
        calories = 0
        continue
    calories += int(line)
top.sort()
print('Part One', maximum)
print('Part Two', sum(top[-3:]))
