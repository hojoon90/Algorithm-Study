n, m = map(int, input().split())
roomList = [];

for i in range(n):
    room = input();
    roomList.append(room)

s, t = map(int, input().split())

roomLocation = 0;
changeLocation = 0;
date = 1;
changeCount = 0;

# 고객이 오는 날짜 동안 만의 room 위치를 확인.
for room in roomList:
    if s <= date < t:
        if s == date :
            roomLocation = room.find('O')  # 도착한 날짜에 맞는 방 위치를 찾아줌.
        # 방이 다 비어있을 수도 있으니 해당 위치 먼저 확인.
        if room[roomLocation] != 'O':
            # 만약 아니면 방 위치 변경
             changeLocation = room.find('O')
             changeCount = changeCount+1
        # TODO 방 위치 변경 시 최소한으로 움직일 수 있는 방을 찾아서 줘야함.

    date = date + 1

print(changeCount)