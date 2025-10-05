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

def possible(goalNum1, goalNum2):
    if goalNum1 == goalNum2:
        return True
    elif goalNum1 > goalNum2:
        return not goalNum1 > (goalNum2+1) * 2 
    else:
        return not goalNum2 > (goalNum1+1) * 2 

testCases = get_int()
for test in range(testCases):
    scoresString = get_string()
    scores = [int(score) for score in scoresString.split(" ")]
    if possible(scores[0], scores[1]) and possible(scores[2] - scores[0], scores[3] - scores[1]):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
