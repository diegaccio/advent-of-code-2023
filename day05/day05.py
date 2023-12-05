import regex as re

example=False   


if not example:
    file1 = open('input.txt', 'r')
else:
    file1 = open('example.txt', 'r')

Lines = file1.readlines()
 

maps = []
mapIdx = -1

#create data
for i in range(len(Lines)):
    line = Lines[i].replace('\n', '')
    #firts line
    if 'seeds:' in line:
        seeds = line.split(':')[1].split(' ')
        seeds.pop(0)
        print(seeds)
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
        range = []
        #src
        range.append(int(coordinates[1]))
        #dst
        range.append(int(coordinates[0]))
        #span
        range.append(int(coordinates[2]))

        #for j in range(0, int(coordinates[2])):
        #    maps[mapIdx][int(coordinates[1]) + j] = int(coordinates[0]) + j
        maps[mapIdx].append(range)
      
#compute locations
lowestLocation = 0
for seed in seeds:
    currentLocation = int(seed)
    print('Checking Seed: {}'.format(currentLocation))
    for map in maps:
        for range in map:
            print(currentLocation)
            print(map)
            if (currentLocation >= range[0]) and (currentLocation <= range[0] + range[2]):
                currentLocation = range[1] + currentLocation - range[0]
                break
    print(currentLocation)
    if (lowestLocation == 0) or (currentLocation < lowestLocation):
        lowestLocation =  currentLocation

print(lowestLocation)  

           
