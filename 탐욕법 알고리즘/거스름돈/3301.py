change = int(input())

changeCount = 0
moneyList = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for money in moneyList:
    changeCount = changeCount + (change // money)
    change = change % money

print(changeCount)