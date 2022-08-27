n = int(input())
m = [int(x) for x in input().split()]

originList = []
for i in range(n):
    originList.append(i)

# dfs 접근

changeList = m

lastLeftCount = 0;
# 오른쪽으로 다시 돌리는 for문 (상위 카운트)
# 접근 방법
# 1. 맨 마지막 왼쪽으로 밀기를 다시 오른쪽으로 민다 (카운트가 제일 늦게 올라감)
# 2. 위치를 서로 바꾸는 작업 실행 (두번째로 늦게 올라가는 카운트)
# 3. 맨처음 왼쪽으로 밀기를 다시 오른쪽으로 민다 (제일 빨리 올라가는 카운트)

while True:
    lastLeftCount += 1
    for j in range(n):
        if(j == 0):
            m.insert(n, m[0])
            m.pop(0)

