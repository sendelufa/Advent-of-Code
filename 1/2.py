filepath = "./input.txt"

cals = []
cal = 0

for line in open(filepath, "r").readlines():
    if not line.strip():
        cals.append(cal)
        cal = 0
        continue

    cal += int(line)

print(sum(sorted(cals)[-3:]))
