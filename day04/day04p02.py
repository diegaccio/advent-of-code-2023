import regex as re

example=False
if not example:
    file1 = open('input.txt', 'r')
else:
    file1 = open('example.txt', 'r')

Lines = file1.readlines()
totalScore = 0 

def checkCard(index):
    cardScore = 0
    print('Checking Card {}'.format(index + 1))
    line = Lines[index].replace('\n', '')
    split = line.split(":")
    sets = split[1].split("|")
    firstSetNumbers = sets[0].split(' ')
    secondSetNumbers = sets[1].split(' ')
    lineScore = 0
    for number in firstSetNumbers:
        if (number != '') and (number in secondSetNumbers):
            lineScore += 1
    if lineScore > 0:
        print('Card Score {}'.format(lineScore))
        for j in range(index + 1, index + lineScore + 1):
            cardScore += checkCard(j)
    return cardScore + 1

# Strips the newline character
for i in range(len(Lines)):
    totalScore += checkCard(i)
    
print(totalScore)


