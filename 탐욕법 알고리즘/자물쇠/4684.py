n = int(input())
m = [int(x) for x in input().split()]

originList = []
for i in range(n):
    originList.append(i)

# dfs 접근

changeList = m

lastLeftCount = 0;


# 바뀐 순서의 위치를 어떻게,,,????
def changeLocation(list):
    wirednumlist = []
    beforenum = 0
    for i in range(n):
        num = list[i]
        if i != n - 1:
            nextnum = list[i + 1]
            if nextnum != num + 1:
                wirednumlist.append(i)

            # 삽입정렬로 위치를 찾아본다?
            for i in range(1, len(x)):
                j, key = i - 1, x[i]
                while x[j] > key and j >= 0:
                    x[j + 1] = x[j]
                    j = j - 1
                    x[j + 1] = key

        # 첫 for문은 저장하고 넘어감
    #     if i == 0:
    #         beforenum = num
    #         continue
    #     # 순서가 맞으면 세팅하고 넘어감
    #     if beforenum == num - 1:
    #         beforenum = num
    #         continue
    #     # 이전 번호가 10이고 그다음이 1이면 정상이므로 num 세팅
    #     elif beforenum == 10 and num == 1 :
    #         beforenum = num
    #     else:
    #         wirednumlist.append(i)
    # return wirednumlist


# 오른쪽으로 다시 돌리는 for문 (상위 카운트)
# 접근 방법
# 1. 맨 마지막 왼쪽으로 밀기를 다시 오른쪽으로 민다 (카운트가 제일 늦게 올라감)
# 2. 위치를 서로 바꾸는 작업 실행 (두번째로 늦게 올라가는 카운트)
# 3. 맨처음 왼쪽으로 밀기를 다시 오른쪽으로 민다 (제일 빨리 올라가는 카운트)

# while True:
lastLeftCount = 5
for j in range(n):
    m.insert(n, m[0])
    m.pop(0)
    print(changeLocation(m))
