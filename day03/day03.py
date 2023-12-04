import regex as re

example=False   


if not example:
    file1 = open('input.txt', 'r')
else:
    file1 = open('example.txt', 'r')

Lines = file1.readlines()
 
count = 0

notSymbols = "1234567890." 
notSymbols = "." 
total = 0
alreadyUsed = []

def checkChar(matrix, y1, x1):
    print("Cecking X {}, Y {}".format(x1, y1))
    ok = not matrix[y1][x1] in notSymbols
    if ok:
        print("Char {}, GOOD".format(matrix[y1][x1] ))
    else:    
        print("Char {}, BAD".format(matrix[y1][x1] ))
    return ok


# Strips the newline character
for i in range(len(Lines)):
    line = Lines[i].replace('\n', '')
    numbers = re.findall('\d+', line)
    #print(line)
    #print(len(line))
    #print(numbers)
    stopXidx = 0
    for number in numbers:
        intNumber = int(number)
        print(number)
        good = False
        count = 0
        #use last numer stopXidx to avoid messing with duplicates on single row 
        startXidx = line.index(number, stopXidx)
        stopXidx = startXidx + len(number)
        if startXidx > 0:
            startXidx -= 1 
        if stopXidx < len(line):
            stopXidx +=1 
        if i > 0:
            startYidx = i -1
        else:
            startYidx = i    
        
        if i < len(Lines) - 1:
            stopYIdx = i + 1
        else:
            stopYIdx = i
        print("startXidx {}, stopXidx {}, startYidx {},stopYIdx {}".format(startXidx, stopXidx, startYidx, stopYIdx))

        for y in range(startYidx, stopYIdx + 1): 
            #if good:
            #    break
            if y != i:
                for x in range(startXidx, stopXidx):
                    if checkChar(Lines, y, x):
                        count += 1
                    #if good:
                    #    break
            else:
                #if ((startXidx != line.index(number)) and (Lines[y][startXidx] == '-')):
                #    intNumber = -intNumber
                #    print('NEGATIVE {}'.format(intNumber))
                #elif ((startXidx != line.index(number)) and (Lines[y][startXidx] == '+')):
                #    intNumber = intNumber
                if ((startXidx != line.index(number)) and checkChar(Lines, y, startXidx)):
                    count += 1
                
                if ((stopXidx != startXidx + len(number)) and checkChar(Lines, y, stopXidx - 1)):
                    count += 1
        good = count > 0
        if good:
            print('{}  GOOD!\n'.format(intNumber))
            total += intNumber
            #if not int(number) in alreadyUsed:
            #    total += int(number)
            #    alreadyUsed.append(int(number))
            #else:
            #    print(number + '  BAD! Already used\n')
        else:
            print(number + '  BAD!\n')


print(total)



           
