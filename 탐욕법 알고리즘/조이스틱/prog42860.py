name = input()
nameArr = list(name)

defaultVal = 65;
count = 0
next = 0

min_move = len(nameArr) - 1

while name[min_move] == 'A' and min_move > 0:
    min_move -= 1

for i, name in enumerate(nameArr):
    nameOrd = ord(name)
    nameDif = nameOrd - defaultVal

    if nameDif > 13:
        count += abs(91 - nameOrd)
    else:
        count += nameDif

    next = i + 1
    while next < len(nameArr) and nameArr[next] == 'A':
        next += 1

    min_move = min(min_move, i + (i + len(nameArr)) - next)

count += min_move
print(count)
