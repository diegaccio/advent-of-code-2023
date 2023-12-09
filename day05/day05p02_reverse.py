
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


#Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35
currentSeed = 0
location = -1

#20283861 too high
#20283860 food
for i in range(0, 1000000000):
#for i in range(0, 99):
    currentSeed = i
    if location > 0:
        break

    print(i)
    for map in reversed(maps):
        #print('map')
        for myrange in map:
            #print(currentSeed)
            #print(myrange)
            if (currentSeed >= myrange[1]) and (currentSeed <= myrange[1] + myrange[2] - 1):
                currentSeed = myrange[0] + currentSeed - myrange[1]
                #print(currentSeed)
                break
    
    #check if current seed is a valid seed       
    for j in range(0, len(seedsRanges), 2):
        #print('Range {} {}'.format(int(seedsRanges[j]), int(seedsRanges[j + 1])))
        if (currentSeed >= int(seedsRanges[j])) and (currentSeed <= int(seedsRanges[j]) + int(seedsRanges[j + 1])):
            location = i
            break    

print(location)


           
