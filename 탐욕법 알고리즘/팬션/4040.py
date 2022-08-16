n, m = map(int, input().split())
roomList = [['X']*m];

for i in range(n):
    room = input();
    roomList.append(room)

s, t = map(int, input().split())

def findOloc(day):
    roomCount = 0;
    for i in range(m):  # 방 위치
        remainCount = 0
        for j in range(day, t): # 날짜
            if roomList[j][i] == 'O':
                remainCount += 1
            else:
                break
        if remainCount > roomCount:
            roomCount = remainCount

    return roomCount

count = -1
today = s

while today<t:
    stay = findOloc(today)
    if stay == 0:
        count = -1
        break

    count+=1
    today+=stay

print(count)
