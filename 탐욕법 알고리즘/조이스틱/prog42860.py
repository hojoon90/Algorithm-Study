name = input()
nameArr = list(name)

defaultVal = 65;
count = 0
i = 0

for name in nameArr:
    nameOrd = ord(name)
    nameDif = nameOrd - defaultVal
    if nameOrd == 65:
        i = i+1
        continue

    if nameDif > 13:
        count += abs(91 - nameOrd)
    else:
        count += nameDif

    if len(nameArr)-1 != i:
        count += 1
    i = i+1

print(count)
