t1, t2= map(int,input().split())

absVal = abs(t1 - t2)

result = 0
result += absVal // 10

rmdVal = absVal % 10
if rmdVal == 1 or rmdVal == 5:
    result += 1
elif rmdVal == 2 or rmdVal == 4 or rmdVal == 6 or rmdVal == 9:
    result += 2
elif rmdVal == 3 or rmdVal == 7 or rmdVal == 8:
    result += 3

print(result)
