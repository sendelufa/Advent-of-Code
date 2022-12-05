filepath = "./input.txt"

r = 0
for line in open(filepath, "r").readlines():
    # map str -> int
    fs, fe, ss, se = map(int, line.strip().replace(",", "-").split("-"))
    fset = set(range(fs, fe+1))
    sset = set(range(ss, se+1))
    if len(set(fset.intersection(sset))) > 0:
        r += 1

print(r)
assert 849 == r, 'Fail'
