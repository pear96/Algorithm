import random

sourceFile = open('output.txt', 'w')

numbers = []

for _ in range(1000000):
    number = random.randrange(1000000)
    numbers.append(number)

print(1000000, file=sourceFile)
print(' '.join(map(str, numbers)), file=sourceFile)
sourceFile.close()