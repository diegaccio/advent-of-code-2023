import regex as re

example=False

if not example:
    file1 = open('input.txt', 'r')
else:
    file1 = open('example.txt', 'r')

Lines = file1.readlines()
 
count = 0

valueList = []

totalValue = 0

# Strips the newline character
for line in Lines:
    soFarSoGood = True
    line = line.replace("\n", "")
    #print(line)
    split = line.split(":")
    gameIdx = int(split[0].split(" ")[1])
    #print(gameIdx)
    gameBag = {}
    sets = split[1].split(";")
    for set in sets:
        setBag = {}
        cubes = set.split(",")
        for cube in cubes:
            values = cube.split(" ")
            if (not values[2] in gameBag) or (gameBag[values[2]] < int(values[1])):
                gameBag[values[2]] = int(values[1])
    print(line)
    print(gameBag)
    gamevalue = 1
    for color in gameBag:
        gamevalue *= gameBag[color]
    print(gamevalue)
    totalValue += gamevalue
print(totalValue)