posX = []
posY = []
answerX, answerY = 0, 0

for _ in range(3):
    x, y = map(int, input().split())
    posX.append(x)
    posY.append(y)

for idx in range(3):
    if posX.count(posX[idx]) == 1:
        answerX = posX[idx]
    if posY.count(posY[idx]) == 1:
        answerY = posY[idx]

print(answerX, answerY)