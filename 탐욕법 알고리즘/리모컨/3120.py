t1, t2= input().split()

t1 = int(t1)
t2 = int(t2)

temp = [10, 5, 1]

i = 0
index = 0

while True:
    if t1 < t2:
        sumCount = t1 + temp[index]
        if sumCount > t2:
            index += 1
        else:
            t1 = sumCount
    else:
        t1 = t1 - temp[index]
        if sumCount < t2:
            index += 1
        else:
            t1 = sumCount

    if t1 == t2:
        break
    i += 1


print(i)
