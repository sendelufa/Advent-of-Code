filepath = "./input.txt"


def rm_duplicates(s):
    n = s[0]
    for char in s[1:]:
        if char != n[-1]:
            n += char
    return n


def find_duplicates(f, s):
    my_set = set([])
    for letter in f:
        if letter in s:
            my_set.add(letter)
            continue
    return list(my_set)


def count_scores(line):
    n = len(line)
    f = rm_duplicates(line[0:n//2])
    s = rm_duplicates(line[n//2:])
    sum = 0
    for ch in find_duplicates(f, s):
        sum += ord(ch)-96 if ord(ch)-96 > 0 else ord(ch)-96+58
    return sum


score_sum = 0
for line in open(filepath, "r").readlines():
    score_sum += count_scores(line)

print(score_sum)
assert 7811 == score_sum, 'Fail'
