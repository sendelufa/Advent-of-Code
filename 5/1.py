filepath = "./input.txt"

desk = {}
moves = []
movesLine = False
for line in open(filepath, "r").readlines():
    if movesLine:
        move = line.strip().split(" ")
        count = int(move[1])
        fr = int(move[3])-1
        to = int(move[5])-1
        moves.append([count, fr, to])
    else:
        for ch in enumerate(line):
            if ch[1] == "1":
                break
            if len(line.strip()) == 0:
                movesLine = True
                break
            if ch[1] != " " and (ch[0] - 1) % 4 == 0:
                index = int(ch[0] / 4)
                if not desk.get(index):
                    desk[index] = []
                desk[index].append(ch[1])


for move in moves:
    for i in range(1, move[0]+1):
        container = desk[move[1]].pop(0)
        desk[move[2]].insert(0, container)

result = ''
for key, value in sorted(desk.items()):
    result += value.pop(0)

print(result)

assert "SBPQRSCDF" == result, 'Fail'
