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
    fieldNum = get_int()
    dandelionFieldsString = get_string()
    dandelionFields = [int(field) for field in dandelionFieldsString.split(" ")]
    oddFields = sorted([field for field in dandelionFields if field % 2 != 0])
    if len(oddFields) == 0:
        sys.stdout.write("0\n")
    else:
        uncutOddFields = len(oddFields) // 2
        total = sum(x for x in dandelionFields if x % 2 == 0)
        total += sum(oddFields[uncutOddFields:])
        sys.stdout.write(str(total) + '\n')
