filepath = "./input.txt"

max_cals = 0
cal = 0

for line in open(filepath, "r").readlines():
    if not line.strip():
        max_cals = cal if cal > max_cals else max_cals
        cal = 0
        continue

    cal += int(line)

print(max_cals)
