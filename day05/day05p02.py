import regex as re

example=False   


if not example:
    file1 = open('input.txt', 'r')
else:
    file1 = open('example.txt', 'r')

Lines = file1.readlines()
 

maps = []
mapIdx = -1
seeds = []

#create data
for i in range(len(Lines)):
    line = Lines[i].replace('\n', '')
    #firts line
    if 'seeds:' in line:
        seedsRanges = line.split(':')[1].split(' ')
        seedsRanges.pop(0)
        print(seedsRanges)

    #
    elif (line == ''):
        if mapIdx >=0:
            print(maps[mapIdx])
        mapIdx +=1
        srcToDest = {}
        ranges = []
        maps.append(ranges) 
        print
    elif line[0].isdigit():
        coordinates = line.split(' ')
        print(coordinates)
        currentrange = []
        #src
        currentrange.append(int(coordinates[1]))
        #dst
        currentrange.append(int(coordinates[0]))
        #span
        currentrange.append(int(coordinates[2]))

        maps[mapIdx].append(currentrange)


#compute locations
lowestLocation = 0
checkedSeeds = []
for i in range(0, len(seedsRanges), 2):
    for j in range(int(seedsRanges[i]), int(seedsRanges[i]) + int(seedsRanges[i + 1])):
        currentLocation = int(j)
        if currentLocation in checkedSeeds:
            continue
        else:
            checkedSeeds.append(currentLocation)
            print('Checking Seed: {}'.format(currentLocation))
            for map in maps:
                for myrange in map:
                    #print(currentLocation)
                    #print(map)
                    if (currentLocation >= myrange[0]) and (currentLocation <= myrange[0] + myrange[2]):
                        currentLocation = myrange[1] + currentLocation - myrange[0]
                        break
            #   print(currentLocation)
            if (lowestLocation == 0) or (currentLocation < lowestLocation):
                lowestLocation =  currentLocation

print(lowestLocation)  

           
