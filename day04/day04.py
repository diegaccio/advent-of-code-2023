import regex as re

example=False

if not example:
    file1 = open('input.txt', 'r')
else:
    file1 = open('example.txt', 'r')

Lines = file1.readlines()
 
totalScore = 0


# Strips the newline character
for line in Lines:
    soFarSoGood = True
    line = line.replace("\n", "")
    print(line)
    split = line.split(":")
    #cardIdx = int(split[0].split(" ")[1])
    #print(cardIdx)
    sets = split[1].split("|")
    firstSetNumbers = sets[0].split(' ')
    secondSetNumbers = sets[1].split(' ')
    print(firstSetNumbers)
    print(secondSetNumbers)
    lineScore = 0
    for number in firstSetNumbers:
        if (number != '') and (number in secondSetNumbers):
            if lineScore == 0:
                lineScore += 1
            else:    
                lineScore *= 2
    totalScore += lineScore
print(totalScore)


