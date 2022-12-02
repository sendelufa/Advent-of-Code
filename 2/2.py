from pyxtension.streams import stream

filepath = "./input.txt"

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors

#   ↱ Scissors ↴
#   Rock  →  Paper

# X - must lose
# Y - must draw
# Z - must win

scoreByResponse = {'X': 1, 'Y': 2, 'Z': 3}
scoreBeat = {'X': 'C', 'Z': 'B', 'Y': 'A'}
scoreLose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
scoreDraw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
scoreWin = {'A': 'Y', 'B': 'Z', 'C': 'X'}


def countScores(round):
    battleScore = 0
    selectedWeapon = ''

    myMove = round[1]
    elfMove = round[0]

    if myMove == 'X':
        selectedWeapon = scoreLose.get(elfMove)
    elif myMove == 'Y':
        selectedWeapon = scoreDraw.get(elfMove)
        battleScore = 3
    else:
        selectedWeapon = scoreWin.get(elfMove)
        battleScore = 6
    return battleScore + scoreByResponse.get(selectedWeapon)


result = sum(stream(open(filepath, "r").readlines())
             .map(lambda line: line.strip().split(' '))
             .map(lambda moveArr: countScores(moveArr))
             .toList())

print(result)
assert 13022 == result, 'Fail'
