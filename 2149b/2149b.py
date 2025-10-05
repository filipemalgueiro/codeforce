import sys
from os import path

FILE = False # Mudar para True para ler de arquivo de input local

if FILE:
    sys.stdin = open(path.join(path.dirname(__file__), 'input.txt'), 'r')
    sys.stdout = open(path.join(path.dirname(__file__), 'output.txt'), 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline()

testCases = get_int()
for test in range(testCases):
    length = get_int()
    numbersString = get_string()
    numbers = [int(number) for number in numbersString.split(" ")]
    numbers.sort()
    maximumDiff = 0
    if length == 2:
        diff = numbers[1] - numbers[0]
        if diff < 0:
            diff = -diff
        sys.stdout.write(str(diff))
        sys.stdout.write('\n')
        continue
    for i in range(1, length//2):
        diff = numbers[i*2 - 1] - numbers[i*2 - 2]
        if diff < 0:
            diff = -diff
        if (maximumDiff < diff):
            maximumDiff = diff
    sys.stdout.write(str(maximumDiff))
    sys.stdout.write('\n')

    

    

 
