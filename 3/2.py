filepath = "./input.txt"


def rm_duplicates(s):
    n = s[0]
    for char in s[1:]:
        if char != n[-1]:
            n += char
    return n


def find_duplicates(f, s):
    result = ""
    for letter in f:
        if letter in s and letter not in result:
            result += letter
            continue
    return result


def count_scores(lines):
    if len(lines) != 3:
        raise Exception("not 3 rucksacks")
    s1_dup = find_duplicates(lines[0], lines[1])
    s2_dup = find_duplicates(lines[1], lines[2])
    sum = 0
    for ch in find_duplicates(s1_dup, s2_dup):
        sum += ord(ch)-96 if ord(ch)-96 > 0 else ord(ch)-96+58
    return sum


score_sum = 0
list_lines = []
i = 1
for line in open(filepath, "r").readlines():
    list_lines.append(line.strip())
    if (i % 3 == 0):
        score_sum += count_scores(list_lines)
        list_lines = []
    i += 1

print(score_sum)
assert 2639 == score_sum, 'Fail'
