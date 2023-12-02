import regex as re

example=False

if not example:
    file1 = open('input.txt', 'r')
else:
    file1 = open('example.txt', 'r')

Lines = file1.readlines()
 
count = 0

#only 12 red cubes, 13 green cubes, and 14 blue cubes
bag = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}


valueList = []

goodLinesCount=0

# Strips the newline character
for line in Lines:
    soFarSoGood = True
    line = line.replace("\n", "")
    #print(line)
    split = line.split(":")
    gameIdx = int(split[0].split(" ")[1])
    #print(gameIdx)
    sets = split[1].split(";")
    for set in sets:
        setBag = {}
        cubes = set.split(",")
        for cube in cubes:
            values = cube.split(" ")
            setBag[values[2]] = int(values[1])
            #print(values)
        #print(setBag)
        for color in setBag:
            soFarSoGood = soFarSoGood and (setBag[color] <= bag[color])
            if not soFarSoGood:
                #print(color)
                #print(setBag[color])
                #print(bag[color])
                break;
        if not soFarSoGood:
            break;
    
    if soFarSoGood:
        goodLinesCount += gameIdx
        print (line + ' GOOD!')
    else:   
        print (line + ' BAD!')
        #print (setBag)    

print(goodLinesCount)