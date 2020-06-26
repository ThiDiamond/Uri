def printChar(idx, first, last):
    try:
        print(first[idx], end='')
    except IndexError:
        print(last[idx], end='')
        return
    try:
        print(last[idx] , end='')
        return
    except IndexError:
        return
n = int(input())
for i in range(n):
    strings = input().split()
    for idx in range(max(len(strings[0]), len(strings[1]))):
        printChar(idx, strings[0], strings[1])
    print()
