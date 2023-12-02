import regex as re

file1 = open('input.txt', 'r')
#file1 = open('example.txt', 'r')
#file1 = open('example2.txt', 'r')
Lines = file1.readlines()
 
count = 0

stringDigits = ['one', 'two', 'three','four', 'five', 'six','seven', 'eight', 'nine']

regex = '[0-9]|' + '|'.join(stringDigits)
#tregex = '[0-9]'
isAStringDigiRegex = '|'.join(stringDigits)
print(regex)

valueList = []

# Strips the newline character
for line in Lines:
    print(line)
    value = ''
    numbers = re.findall(regex, line, overlapped=True)
    if len(numbers) > 0:
        for i in [0, -1]:
            if re.search(isAStringDigiRegex,numbers[i]):
                value += str(stringDigits.index(numbers[i]) + 1)
            else:
                value += numbers[i]
        valueList.append(int(value))

    print(valueList[-1])
    print( sum(valueList))
    print()

print('Total: ')
print( sum(valueList))