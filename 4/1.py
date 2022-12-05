filepath = "./input.txt"

r = 0
for line in open(filepath, "r").readlines():
    # map str -> int
    fs, fe, ss, se = map(int, line.strip().replace(",", "-").split("-"))
    print(fs, fe, ss, se)
    if fs <= ss and fe >= se or ss <= fs and se >= fe:
        r += 1

print(r)
assert 487 == r, 'Fail'
