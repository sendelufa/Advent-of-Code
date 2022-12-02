filepath = "./input.txt"

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors

#   ↱ Scissors ↴
#   Rock  ←  Paper

scoreByResponse = {'X': 1, 'Y': 2, 'Z': 3}
scoreBeat = {'X': 'C', 'Z': 'B', 'Y': 'A'}


def countScores(round):
    battleScore = 0
    myMove = round[1]
    elfMove = round[0]

    if ord(elfMove) is (ord(myMove) - 23):
        battleScore = 3
    elif scoreBeat.get(myMove) is elfMove:
        battleScore = 6

    return battleScore + scoreByResponse.get(myMove)


scoreSum = 0
for line in open(filepath, "r").readlines():
    round = line.strip().split(' ')
    scoreSum += countScores(round)
print(scoreSum)

assert 11841 == scoreSum, 'Fail'
