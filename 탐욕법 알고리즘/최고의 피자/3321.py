import math

array = []
topingCnt = int(input())
douPrice, topingPrice= map(int, input().split())
douCalories = int(input())
for i in range(topingCnt):
    array.append(int(input()))

# 토핑을 하나씩 더하면서 평균이 가장 높은 값을 출력해줌.
array.sort(reverse=True)

avg = douCalories / douPrice
calories = douCalories
coast = 0

for j in array:
    calories += j
    coast += topingPrice
    totalPrice = douPrice + coast

    compAvg = calories / totalPrice
    if compAvg > avg:
        avg = compAvg

print(math.trunc(avg))